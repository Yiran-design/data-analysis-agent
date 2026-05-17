import streamlit as st
import pandas as pd

from agent.multi_agent import run_agent
from agent.reporter import generate_report

st.set_page_config(page_title="Data Analysis Agent")
st.title("📊 Data Analysis Agent")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
question = st.text_input("Enter your analysis question")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.dataframe(df.head())

    if st.button("Run Analysis"):
        with st.spinner("Agent is thinking..."):
            result = run_agent(df, question)
            report = generate_report(question, result)

        st.subheader("Agent Reasoning")
        st.text(result)

        st.subheader("Final Report")
        st.write(report)
