import spacy
from pyresparser import ResumeParser

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Use ResumeParser
data = ResumeParser("C:/Users/User/Documents/Keerthana S-2112019-CSE-NEC.pdf").get_extracted_data()

print(data)
