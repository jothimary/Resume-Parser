import PyPDF2
from docx import Document
import os
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_resume(resume_path):
    _, file_extension = os.path.splitext(resume_path)
    
    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(resume_path)
    elif file_extension.lower() == '.docx':
        return extract_text_from_docx(resume_path)
    else:
        print("Unsupported file format. Please provide a PDF or DOCX file.")

def extract_information_from_resume(text):
    # Regular expressions for name, email, phone number, and skills
    name_pattern = re.compile(r'\b(?:Name|Full Name)[:\s]*([^\n\r]+)', re.IGNORECASE)
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_pattern = re.compile(r'\b(?:\+\d{1,2}\s?)?(?:\(\d{1,4}\))?(?:[\s.-]?\d{1,15})\b')
    skills_pattern = re.compile(r'\b(?:Skills|Technical Skills)[:\s]*([^\n\r]+)', re.IGNORECASE)

    # Extract information
    name_match = re.search(name_pattern, text)
    email_match = re.search(email_pattern, text)
    phone_match = re.search(phone_pattern, text)
    skills_match = re.search(skills_pattern, text)

    # Get matched values or return None if not found
    name = name_match.group(1) if name_match else None
    email = email_match.group() if email_match else None
    phone = phone_match.group() if phone_match else None
    skills = skills_match.group(1) if skills_match else None

    return name, email, phone, skills

# Example usage:
resume_path = r"C:\xampp\htdocs\Resspar\KEERTHANA S resume.pdf"
text_from_resume = extract_text_from_resume(resume_path)
name, email, phone, skills = extract_information_from_resume(text_from_resume)

print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills)
