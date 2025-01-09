from pyresparser import ResumeParser

# Resume file path
resume_path = "C:/Users/User/Documents/Keerthana S-2112019-CSE-NEC.pdf"  # Replace with the path to your resume file

# Initialize ResumeParser object with the resume path
parser = ResumeParser(resume_path)

# Parse resume
resume_data = parser.get_extracted_data()

# Print parsed data
print(resume_data)
