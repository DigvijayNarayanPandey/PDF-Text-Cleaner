# PDF Text Extractor and Cleaner

This project provides a simple tool to extract text from PDF files, clean the extracted text by removing stopwords, punctuation, numbers, and special characters, and perform lemmatization. The cleaned text is then saved to a CSV file.

## Features

- Extract text from PDF files using `pdfplumber`.
- Clean the extracted text by:
  - Converting to lowercase.
  - Removing punctuation.
  - Removing stopwords.
  - Performing tokenization and lemmatization.
  - Removing numbers and special characters.
  - Removing extra whitespaces.
- Save the cleaned text to a CSV file using `pandas`.

## Requirements

- Python 3.x
- pdfplumber
- pandas
- nltk

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pdf-text-extractor.git
   cd pdf-text-extractor
