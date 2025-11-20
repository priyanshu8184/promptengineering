import streamlit as st
from langchain_groq  import ChatGroq

GROQ_API_KEY= "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"
llm= ChatGroq(groq_api_key= GROQ_API_KEY,model_name="llama-3.3-70b-versatile")

#text box

prompt= st.text_input("Enter Your Question Please.")

#button is created
button= st.button("ASK NOW")

#if button is clicked
if button:
    response = llm.invoke(prompt)

    #show the output
    st.info(response.content)

