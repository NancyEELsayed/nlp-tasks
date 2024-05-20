import nltk
import spacy
from nltk import pos_tag 

# 1-
text_token=input("Enter text in Spanish:- ")
print(nltk.sent_tokenize(text_token))
nlp=spacy.load('es_core_news_sm')
text_doc=nlp(text_token)
text_sent=[sentence.text for sentence in text_doc.sents]
print(text_sent)


# 2-
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
nltk.download('punkt')

def pos_tagging_penn_treebank(text):
    tokens = nltk.word_tokenize(text)
    penn_tags = pos_tag(tokens)
    return penn_tags

def pos_tagging_universal(text):
    tokens = nltk.word_tokenize(text)
    universal_tags = pos_tag(tokens, tagset='universal')
    return universal_tags

def compare_pos_tags(text):
    penn_tags = pos_tagging_penn_treebank(text)
    universal_tags = pos_tagging_universal(text)
    print(penn_tags,universal_tags)

if __name__ == "__main__":
    text = input("Enter the text for POS tagging: ")
    compare_pos_tags(text)

# 3-
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def list_stopwords():
    languages = stopwords.fileids()
    
    for language in languages:
        print(f"Stop words in {language}:")
        print(stopwords.words(language))
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    list_stopwords()



