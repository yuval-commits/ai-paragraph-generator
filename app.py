import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyBfTS90lbCckKhGshGcpUT_8gEgCdXsFO4")

st.title("AI Paragraph Generator (Gemini 2.5 Flash)")

st.write("Enter a topic and generate a short AI paragraph.")

user_input = st.text_input("Enter a topic:")

if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Please enter something.")
    else:
        try:
            model = genai.GenerativeModel("models/gemini-2.5-flash")

            response = model.generate_content(
                f"Write a short paragraph about {user_input}"
            )

            st.success("Generated Content:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
