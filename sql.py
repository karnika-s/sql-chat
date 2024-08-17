# frontenend streamlit file 
# fetches the data drom db, converts human query 
# and displays it to page 

from dotenv import load_dotenv
load_dotenv() # load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai


# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):             #telling model how to behave
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, 
    GRADES,MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENTS 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """

]

#Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("😎 My SQL Assistant")
st.markdown("<h1>😎 My SQL Assistant - by Karnika</h1>", unsafe_allow_html=True)
st.write("----------------------------------------------------------------")

question=st.text_input("Input - Students DB is used: ",key="input")

submit=st.button("Shoot your question...")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"students.db")
    # st.subheader("Your Response is : ")
    st.markdown("<h4> Your results: </h4>" , unsafe_allow_html=True)
    st.write("----------------------------------------------------------------")
    for row in response:
        print(row)
        # st.write(row)
        # st.subheader(row)
        st.markdown(f"<h6>{row}</h6>", unsafe_allow_html=True)
        st.write("----------------------------------------------------------------")




