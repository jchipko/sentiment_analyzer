import re
import pickle

import yaml
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

with open('config/config.yml', 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)

def get_prediction(text):
    """
    Predicts sentiment of input text, along with a
    confidence score for both the negative and positive classes
    """

    loaded_model = pickle.load(open(config['MODEL_PATH'], 'rb'))
    preprocessed_text = preprocess_text(text)

    class_prediction = loaded_model.predict([preprocessed_text])[0]
    confidence = loaded_model.predict_proba([preprocessed_text])
    negative_confidence = confidence[0][0]
    positive_confidence = confidence[0][1]

    return class_prediction, negative_confidence, positive_confidence

def preprocess_text(text):
    """Cleans and lemmatizes text input by user"""

    # lowercase the text
    text = text.lower()

    # remove special characters
    pattern = r'[^a-zA-Z0-9\s]|\[|\|\\W]'
    text = re.sub(pattern, '', text)

    # create stop word list
    stop_words = stopwords.words('english')
    stop_words = [word for word in stop_words if word not in config['STOPWORDS_TO_REMOVE']]
    stop_words = set(stop_words).union(config['STOPWORDS_TO_ADD'])

    # lemmatize and remove stop words
    lemmatizer = WordNetLemmatizer()
    text = [lemmatizer.lemmatize(w) for w in word_tokenize(text) if not w in stop_words]

    # join all
    text = " ".join(text)

    return text