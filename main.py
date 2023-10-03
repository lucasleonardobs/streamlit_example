import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Python é melhor que JavaScript")

df = pd.read_csv("data/alunos.csv")

fig = px.bar(df["Motivo_Evasão"].value_counts().reset_index(), x='Motivo_Evasão', y='count')

st.plotly_chart(fig)