import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class Preprocessor:
    @staticmethod
    def preprocess(article_data):
        processed_data = {}
        processed_data['title'] = Preprocessor.preprocess_text(article_data['title'])
        processed_data['text'] = Preprocessor.preprocess_text(article_data['text'])

        return processed_data

    @staticmethod
    def preprocess_text(text):
        # Tokenization
        tokens = word_tokenize(text)

        # Lowercasing
        tokens = [token.lower() for token in tokens]

        # Removing stop words
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

        # Removing punctuation and special characters (except for full stops)
        tokens = [token for token in tokens if token.isalpha() or token == '.']

        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        return tokens