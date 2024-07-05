import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import random

# Download NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a simple chatbot created using NLTK.",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that. Can you rephrase?"
}

# Preprocess function
def preprocess(text):
    text = text.lower()  # Lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english')]  # Lemmatize and remove stopwords
    return tokens

# Generate response function
def generate_response(user_input):
    tokens = preprocess(user_input)
    if not tokens:
        return responses["default"]
    processd_text = ' '.join(tokens)
    
    for token in tokens:
        if token in responses:
            return responses[token]
    
    return responses["default"]

# Chatbot function
def chatbot():
    print("Chatbot: Hello! How can I help you today? (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot:", responses["bye"])
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

# Run chatbot
chatbot()
