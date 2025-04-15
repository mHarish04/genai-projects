import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client with API key
client = openai.OpenAI(api_key=api_key)

st.title("📄 Smart Resume Analyzer")
resume = st.text_area("Paste your resume here")

if st.button("Analyze"):
    if resume:
        with st.spinner("Analyzing with GenAI..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Analyze this resume:\n{resume}"}
                ]
            )
            st.success("Done!")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Please paste your resume.")
