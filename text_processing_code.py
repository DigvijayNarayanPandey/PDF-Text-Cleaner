import pdfplumber
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure necessary resources are downloaded
nltk.download('stopwords')
nltk.download('wordnet')

# Step 1: Function to extract text from PDF

def extract_text_from_pdf(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Step 2: Function to clean the text

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    # Tokenization
    words = text.split()
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Remove numbers and special characters
    words = [re.sub(r'[^a-zA-Z]', '', word)
             for word in words if not word.isdigit()]
    # Remove extra whitespaces
    cleaned_text = ' '.join(words).strip()
    return cleaned_text


# Step 3: Extract and clean text
# Replace with your input PDF file path
pdf_file_path = r"Image Processing.pdf"
extracted_text = extract_text_from_pdf(pdf_file_path)  # Extract text from PDF
cleaned_text = clean_text(extracted_text)  # Clean the extracted text

# Step 4: Print the cleaned text
print(cleaned_text)

# Step 5: Save the cleaned text to a CSV
cleaned_data = pd.DataFrame({'cleaned_text': [cleaned_text]})
cleaned_data.to_csv('cleaned_pdf_text.csv', index=False)