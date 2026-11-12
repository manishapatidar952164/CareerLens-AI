# CareerLens AI – Resume Analyzer

A web-based resume analysis application built using Python and Flask. CareerLens AI compares a candidate's resume with a job description and identifies matching and missing skills.

## 🌐 Live Demo
https://careerlens-ai-y7eh.onrender.com

## ✨ Features
- Upload resumes in PDF and DOCX formats.
- Extract text from uploaded resumes.
- Compare resume skills with job requirements.
- Calculate a skill match percentage.
- Identify matched and missing skills.
- Provide resume improvement suggestions.
- Clean and responsive user interface.

## 🛠️ Tech Stack
- Python
- Flask
- HTML5
- CSS3
- PyMuPDF
- python-docx
- Gunicorn
- Git and GitHub
- Render

## ⚙️ How It Works
1. Upload your resume.
2. Paste the target job description.
3. The application extracts text from the resume.
4. It identifies skills in both documents.
5. It calculates the percentage of matching detected skills.
6. It displays the analysis report and recommendations.

**Note:** The current version uses keyword-based skill matching. The match score measures detected skill overlap; it does not predict hiring probability or fully evaluate resume quality.

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/manishapatidar952164/CareerLens-AI.git
cd CareerLens-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## 🚀 Future Improvements
- Semantic resume matching.
- Experience and education analysis.
- Downloadable PDF reports.
- More personalized recommendations.

## 👩‍💻 Developer
Manisha Patidar

## 🔗 Project Links
- [Live Website](https://careerlens-ai-y7eh.onrender.com)
- [GitHub Repository](https://github.com/manishapatidar952164/CareerLens-AI)
