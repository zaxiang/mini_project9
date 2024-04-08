import streamlit as st
from transformers import pipeline

# Custom CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Background color of the button */
        color: white; /* Text color of the button */
        font-size: 16px; /* Button text size */
    }
    .stButton>button:hover {
        background-color: #45a049; /* Button color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up title and user input
st.title('Text Generation Tool')
user_input = st.text_input("Enter your text:", "Type here")

if st.button('Generate Text'):
    # Load the model
    generator = pipeline('text-generation', model='gpt2')
    # Generate text
    generated = generator(user_input, max_length=300, num_return_sequences=1)
    # Display generated text
    st.write(generated[0]['generated_text'])