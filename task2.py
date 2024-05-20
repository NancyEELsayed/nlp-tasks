import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def tokenize_and_stem(text):
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens


def process_csv_file(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) 
            for row in csv_reader:
                text = row[0]  
                tokens = tokenize_and_stem(text)
                print(tokens)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'emotion.csv'  
process_csv_file(file_path)

