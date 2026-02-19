import streamlit as st
import google.generativeai as genai

# Configure page
st.set_page_config(
    page_title="AI Paragraph Generator",
    page_icon="✨",
    layout="centered"
)

# Configure Gemini
genai.configure(api_key="AIzaSyC-30GIfF_Xu83TJgKcZXvMG8oL8a7mQn8")

st.title("✨ AI Content Generator")
st.markdown("Generate high-quality AI content using Gemini 2.5 Flash.")

st.divider()

# User Inputs
topic = st.text_input("Enter your topic:")

tone = st.selectbox(
    "Select tone:",
    ["Professional", "Casual", "Creative", "Motivational"]
)

length = st.slider(
    "Select length (approximate word count):",
    min_value=50,
    max_value=300,
    value=120,
    step=10
)

st.divider()

# Generate Button
if st.button("Generate Content 🚀"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        try:
            model = genai.GenerativeModel("models/gemini-2.5-flash")

            prompt = f"""
            Write a {tone.lower()} paragraph about: {topic}.
            Keep it around {length} words.
            Make it clear, engaging, and well-structured.
            """

            with st.spinner("Generating content..."):
                response = model.generate_content(prompt)

            st.success("Generated Content:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Built using Streamlit + Google Gemini API")
