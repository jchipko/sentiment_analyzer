import streamlit as st

from utils import get_prediction

st.title('Movie Review Sentiment Analyzer')
st.info(
    "Enter a movie review and the app will predict whether your review is positive or negative."
)
user_input = st.text_area("Enter movie review here")

if user_input:
    prediction, negative_confidence, positive_confidence = get_prediction(user_input)
    if negative_confidence > .7 or positive_confidence > .7:
        st.write(f"Prediction: the sentiment of this review is {prediction}.")
    else:
        st.write("The result is inconclusive. Cannot make a prediction.")
