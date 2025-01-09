import PyPDF2
from docx import Document
import os

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

# Example usage:
resume_path = r"C:\xampp\htdocs\Resspar\KEERTHANA S resume.pdf"
text_from_resume = extract_text_from_resume(resume_path)
print(text_from_resume)
