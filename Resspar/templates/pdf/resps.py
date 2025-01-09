from resume_parser import resumeparse

# Resume file path
resume_path = 'Keeres.pdf'  # Replace with the path to your resume file

# Parse resume
resume_data = resumeparse.read_file(resume_path)

# Print parsed data
print(resume_data)
