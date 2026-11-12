


from flask import Flask, render_template, request
import fitz
from docx import Document
from io import BytesIO

app = Flask(__name__)

# Maximum upload size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Skills database
SKILLS = [
    "python", "java", "c++", "c", "javascript",
    "html", "css", "react", "node.js", "flask",
    "django", "sql", "mysql", "mongodb",
    "machine learning", "deep learning",
    "artificial intelligence", "data analysis",
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch",
    "data structures", "algorithms",
    "git", "github", "excel", "communication"
]


# Extract text from PDF or DOCX
def extract_resume_text(file):

    filename = file.filename.lower()
    file_bytes = file.read()

    if filename.endswith(".pdf"):
        pdf = fitz.open(
            stream=file_bytes,
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text() + "\n"

        pdf.close()
        return text

    elif filename.endswith(".docx"):
        document = Document(BytesIO(file_bytes))

        return "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

    return ""


# Find skills in text
def find_skills(text):

    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# FEATURES PAGE
@app.route("/features")
def features():
    return render_template("features.html")


# ANALYZER PAGE
@app.route("/analyzer")
def analyzer():
    return render_template("analyzer.html")


# RESUME ANALYSIS
@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description", "")

    if not resume or not resume.filename:
        return "Please upload your resume."

    if not resume.filename.lower().endswith((".pdf", ".docx")):
        return "Please upload a PDF or DOCX file."

    if not job_description.strip():
        return "Please enter a job description."

    try:
        resume_text = extract_resume_text(resume)

        if not resume_text.strip():
            return "Could not extract text. Please upload a readable PDF or DOCX."

        # Detect skills
        resume_skills = find_skills(resume_text)
        job_skills = find_skills(job_description)

        # Compare skills
        matched_skills = [
            skill for skill in job_skills
            if skill in resume_skills
        ]

        missing_skills = [
            skill for skill in job_skills
            if skill not in resume_skills
        ]

        # Calculate match percentage
        if job_skills:
            match_percentage = round(
                len(matched_skills) / len(job_skills) * 100
            )
        else:
            match_percentage = 0

        # Resume strength
        if match_percentage >= 75:
            resume_strength = "Strong"
        elif match_percentage >= 45:
            resume_strength = "Moderate"
        else:
            resume_strength = "Needs Work"

        # Generate insights
        if matched_skills:
            strengths = (
                "Your resume includes these relevant skills: "
                + ", ".join(matched_skills)
                + "."
            )
        else:
            strengths = (
                "No matching skills were detected. "
                "Review your resume to ensure your relevant skills are included."
            )

        if missing_skills:
            improvements = (
                "The following job-related skills were not found in your resume: "
                + ", ".join(missing_skills)
                + "."
            )
        else:
            improvements = (
                "All detected job skills were found in your resume. "
                "You can further improve your project descriptions and achievements."
            )

        recommendations = []

        if missing_skills:
            recommendations.append(
                "If you genuinely have experience with these skills, "
                "include them clearly in your resume: "
                + ", ".join(missing_skills) + "."
            )

        recommendations.append(
            "Add measurable results and achievements to your project descriptions."
        )

        recommendations.append(
            "Keep your resume clear, organized and relevant to the job role."
        )

        return render_template(
            "result.html",
            match_percentage=match_percentage,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            resume_strength=resume_strength,
            strengths=strengths,
            improvements=improvements,
            recommendations=recommendations
        )

    except Exception as error:
        print("Analysis error:", error)
        return "Something went wrong while analyzing your resume. Please try another file."


# File size error
@app.errorhandler(413)
def file_too_large(error):
    return "File is too large. Please upload a file under 5 MB.", 413


# START SERVER
if __name__ == "__main__":
    app.run(debug=True)
