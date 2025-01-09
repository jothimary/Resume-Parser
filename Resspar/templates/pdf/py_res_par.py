from pyresparser import ResumeParser

# Resume file path
resume_path = 'Keeres.pdf'

# Initialize ResumeParser object with the resume path
parser = ResumeParser()

# Parse resume
resume_data = parser.extract_resume()

# Print parsed data
print(resume_data)
