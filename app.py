
from flask import Flask, render_template, request, send_file
from pypdf import PdfReader
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from analyzer import analyze_resume, analyze_ats_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def create_pdf_report(score, resume_skills, matched, missing):
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=A4)

    pdf.drawString(50, 800, "AI Resume Analyzer Report")
    pdf.drawString(50, 760, f"Resume Match Score: {score}%")

    y = 720

    sections = [
        ("Skills Found:", resume_skills),
        ("Matched Skills:", matched),
        ("Missing Skills:", missing)
    ]

    for heading, skills in sections:
        if y < 80:
            pdf.showPage()
            y = 800

        pdf.drawString(50, y, heading)
        y -= 25

        for skill in skills:
            if y < 60:
                pdf.showPage()
                y = 800

            pdf.drawString(70, y, f"- {skill}")
            y -= 20

        y -= 10

    pdf.save()
    pdf_buffer.seek(0)
    return pdf_buffer


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description", "").strip()

    if resume is None or resume.filename == "":
        return "Please upload your resume PDF!"

    if not resume.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed!"

    if not job_description:
        return "Please enter Job Description!"

    try:
        pdf = PdfReader(BytesIO(resume.read()))

        if len(pdf.pages) == 0:
            return "Your PDF is empty!"

        resume_text = ""

        for page in pdf.pages:
            resume_text += page.extract_text() or ""

        if not resume_text.strip():
            return "No readable text found in PDF!"

    except Exception:
        return "Invalid or corrupted PDF file!"
    resume_skills    , matched, missing, score = analyze_resume(
        resume_text, job_description
    )

    ats_score    , ats_suggestions = analyze_ats_resume(resume_text)

    return render_template    (
        "result.html"        ,
        resume_skills=resume_skills        ,
        matched=matched        ,
        missing=missing        ,
        score=score        ,
        ats_score=ats_score        ,
        ats_suggestions=ats_suggestions
    )


@app.route("/download-report")
def download_report():

    score = request.args.get("score", default=0, type=float)
    resume_skills = request.args.getlist("resume_skills")
    matched = request.args.getlist("matched")
    missing = request.args.getlist("missing")

    pdf_buffer = create_pdf_report(
        score, resume_skills, matched, missing
    )

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="Resume_Analysis_Report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
