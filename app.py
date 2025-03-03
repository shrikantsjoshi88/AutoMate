import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-2.0-flash") 
# chat = model.start_chat()
# Define the function to generate test cases using Gemini
def generate_test_cases(requirement):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use appropriate Gemini model
        response = model.generate_content(requirement)
        return response.text  # Extract the generated text
    except Exception as e:
        return str(e)

# Streamlit app layout

st.title('TestMate - Your AI-powered test case wizard!')

st.write('Calling all testers! Enter your software requirements and let the magic of test case generation begin!')

# Text area for user to enter the software requirement

requirement = st.text_area("Requirement", height=150)

# Button to generate test cases

if st.button('Generate Test Cases'):

    if requirement:

        with st.spinner('Hold on tight... Test cases are brewing!'):

            try:

                test_cases = generate_test_cases(requirement)

                st.success('Boom! Test cases have been successfully generated! Now go forth and test like a champ!')

                st.write(test_cases)

            except Exception as e:

                st.error('Oops! An error crashed the party while generating test cases! Time to debug and save the day!')

                st.error(e)

    else:

        st.error('Enter a requirement and let the test cases roll in!')

st.write('Caution! Test cases ahead! Review them carefully, tweak as needed and make sure no critical scenarios slip through the cracks')
