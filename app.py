import streamlit as st

import google.generativeai as genai

import os

# Retrieve the API key from the environment variable

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the Gemini API key

genai.configure(api_key=GEMINI_API_KEY)

# Define the function to generate test cases

# Define the function to generate test cases using Gemini
def generate_test_cases(requirement):
    try:
        model = genai.GenerativeModel("gemini-pro")  # Use appropriate Gemini model
        response = model.generate_content(requirement)
        return response.text  # Extract the generated text
    except Exception as e:
        return str(e)

# Streamlit app layout

st.title('TestMate – Your AI-powered test case wizard!')

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

        st.error('Please enter a requirement to generate test cases.')

st.write('Caution - Review these test cases carefully and modify or update them as per your project-specific requirements.Ensure that all critical scenarios are covered to avoid gaps in testing')
