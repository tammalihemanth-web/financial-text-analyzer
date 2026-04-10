import streamlit as st
from textblob import TextBlob

st.title("Financial Text Analyzer")

text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if text:
        blob = TextBlob(text)

        polarity = round(blob.sentiment.polarity, 3)
        subjectivity = round(blob.sentiment.subjectivity, 3)

        if polarity > 0:
            trend = "Positive"
        elif polarity < 0:
            trend = "Negative"
        else:
            trend = "Neutral"

        if polarity > 0.2:
            result = "Strong Positive"
        elif polarity > 0:
            result = "Mild Positive"
        elif polarity < -0.2:
            result = "Strong Negative"
        elif polarity < 0:
            result = "Mild Negative"
        else:
            result = "Neutral"

        word_count = len(text.split())
        keywords = ["growth", "risk", "profit", "loss", "market"]
        found_keywords = []

        text_lower = text.lower()
        for word in keywords:
            if word in text_lower or word + "s" in text_lower:
                found_keywords.append(word)

        st.subheader("Analysis Result")
        st.write("Polarity Score:", polarity)
        st.write("Subjectivity:", subjectivity)
        st.write("Word Count:", word_count)
        st.write("Sentiment:", result)
        st.write("Trend:", trend)

        if found_keywords:
            st.write("Keywords:", ", ".join(found_keywords))
        else:
            st.write("Keywords: None found")

        st.write("Keyword Count:", len(found_keywords))
    else:
        st.warning("Please enter some text")