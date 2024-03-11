import nltk
# nltk.download()
# from Nltk import sent_tokenize
# print(nltk.sent_tokenize("hello world. welcome"))
# -----------------------------------------------------------------------------
# task1:-
def tokenize_words(text):
    word = nltk.word_tokenize(text)
    print("Tokenized Words:")
    print(word)

def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    print("Tokenized Sentences:")
    print(sentences)

def split_text(text):
    split_output = text.split()
    print("Split Output:")
    print(split_output)

user_text = input("Enter some text: ")

print("Choose an option:")
print("1. Print tokenized words")
print("2. Print tokenized sentences")
print("3. Print output using split function")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == '1':
    tokenize_words(user_text)
elif choice == '2':
    tokenize_sentences(user_text)
elif choice == '3':
    split_text(user_text)
else:
    print("Invalid choice. Please choose a valid option.")