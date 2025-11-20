import streamlit as st
from langchain_groq import ChatGroq

GROQ_API_KEY= "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"
llm= ChatGroq(groq_api_key= GROQ_API_KEY,model_name="llama-3.3-70b-versatile")
prompt= """

<Role> 
you are an experienced editor of a news channel , who have expertise in providing the quick and short summary of the news 
without losing the actualm essence of the news. 
</Role>


<Objective>
The generted summary will be published on the website of the news channel to enhance the traffic of the users.
</Objective>


<input_Description>
The input is provided below . It is the long detailed news by the anchors and by the reporters.

#input news : [ INPUT NEWS ]
</input_Description>


<Instruction>
1. Write the crisp and small summary consisting all important deatils.
2. Focus on the date and time from the news.
3. Do not be biased towards any race ,political party, gender etc.
</Instruction>

<Output_Format>
The output must be in the form of a paragraph with some bullets points highlighting the key events or details.
</Output_Format>
"""
news= st.text_input("enter the news")

prompt = prompt.replace("[INPUT NEWS]",news)
#Create a button
button =st.button("ASK")
if button:
    response= llm.invoke(prompt)
    st.write(response.content)