import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))
#get file into filename

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath, encoding="utf-8") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]
#remove ".txt" & "diary/" in filename, just keep "date" part

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)


