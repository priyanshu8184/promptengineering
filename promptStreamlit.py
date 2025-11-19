import streamlit as st
from langchain_groq import ChatGroq
#install streamlit , langchain, langchain_groq


GROQ_API_KEY= "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"
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="llama-3.3-70b-versatile")

st.header("LLM Powered AI ChatBot")
#text box
Query = st.text_input("Enter the Query")
#prompt is written so that llm gives the correct and concise answer.
prompt = f"""
<query>
{Query}
</query>
<Role>
You are an experienced career advisor specialised in helping students and early
professionals plan their learning paths.
</Role>

<Objective>
Provide meaningful and satisfactory career guidance, resume suggestions, 
and predictable advice that align with the users educational background, knowledge, and skill level.
</Objective>

<Input_Description>
The input is provided below . It is the long detailed query by the user.

#input User : [ INPUT USER ]
</Input_Description>

<Instruction>
1. Analyze the query their education, knowledge. 
2. Suggest a clear, crisp, resume tips. 
3. Be presice and give small point wise answer.   
</Instruction>

<Output_Format>
output will be in the form of bullet point. with highlighting the most including lines or points in their resume.
</Output_Format>


"""
prompt =  prompt.replace("[INPUT QUERY]", Query)
#Create a button
button = st.button("SUBMIT")

#if button is clicked
if button:
    response = llm.invoke(prompt)

    #show the output
    st.write(response.content)
