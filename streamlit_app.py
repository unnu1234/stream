import streamlit as st

st.title("AI Elite Streamlit Demo")

st.header("Session for Elite-18")

st.subheader("by Lakshmi Teja")

name = st.text_input("Please enter your name:")

st.write(f"Hello, {name}! Welcome to the session")

course = st.radio("Select your course",['Data Analysis','Data Science','Full Stack'])

no_of_months = st.number_input("How many months would you like to dedicate for completing the course?")

st.write(f"You have opted for {course}. You decided to complete the course in {no_of_months} months time period.")

ratings = st.slider(f"Choose your ratings for the {course}",min_value=1.0,max_value=5.0,step=0.5,)

st.write(f"You have given {ratings} rating to the course")
