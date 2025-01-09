import textract 
 
# Extract text from PDF 
resume_text = textract.process("C:/xampp/htdocs/Resspar/Keeres.pdf").decode('utf-8') 
