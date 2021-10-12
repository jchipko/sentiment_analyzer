# Sentiment Analyzer

This repo contains an implementation of a movie review sentiment analyzer. When given the text of a movie review, the model will predict whether the review is positive or negative. However, for cases in which the confidence of the model's prediction is low, the app will return the following wording: *"The result is inconclusive. Cannot make a prediction."* 

# Web Application
Explore the sentiment analyzer app on Streamlit Sharing: https://share.streamlit.io/jchipko/sentiment_analyzer/main/app.py

## Installation and Running

Clone the repo:

```
git clone https://github.com/jchipko/sentiment_analyzer.git
```

Navigate to the directory:

```buildoutcfg
cd sentiment_analyzer
```

Install dependencies:
1. Create a Python virtual environment with version 3.8 and activate it
2. Install libraries using the following command:
```buildoutcfg
pip install -r requirements.txt
```

To run the app, use the following command:

```buildoutcfg
streamlit run app.py
```