from flask import Flask, render_template, request
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return 'No file uploaded'

    resume = request.files['resume']
    if resume.filename == '':
        return 'No selected file'

    # Parse resume using SpaCy
    parsed_data = parse_resume(resume)

    # Render parsed data in HTML template
    return render_template('result.html', resume_data=parsed_data)

def parse_resume(resume):
    # Read resume text
    resume_text = resume.read()

    # Perform parsing using SpaCy
    doc = nlp(resume_text)

    # Extract relevant information
    # Example: Extracting names
    names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']

    return {'names': names}  # Return parsed data as dictionary

if __name__ == '__main__':
    app.run(debug=True)
