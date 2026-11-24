
# AI Resume Analyzer

AI Resume Analyzer is a Python Flask-based web application that analyzes a resume and compares its skills with a given job description.

## Features

- Upload resume in PDF format
- Extract text from PDF
- Identify skills from resume
- Match resume skills with job description
- Calculate resume match score
- Display matched and missing skills
- Download analysis report as PDF
- Basic error handling for invalid files

## Technologies Used

- Python
- Flask
- HTML
- CSS
- pypdf
- ReportLab

## Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── analyzer.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
```

## Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

2. Open the project folder:

```bash
cd AI-Resume-Analyzer
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open this URL in your browser:

```text
http://127.0.0.1:5000/
```

## How to Use

1. Upload your resume PDF.
2. Paste the job description.
3. Click on Analyze Resume.
4. View your match score and skills analysis.
5. Download the PDF report.

## Author

Aakarsh Kumar

B.Tech CSE (Artificial Intelligence)
