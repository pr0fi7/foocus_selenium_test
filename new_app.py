import streamlit as st
from main import send_prompt

prompt = st.text_input("Enter your prompt here:")
generate_button = st.button("Generate Image")
headless = st.checkbox("Headless Mode", value=False)

url = "https://d129369a4ac8f84e30.gradio.live/"
json_link = "https://d129369a4ac8f84e30.gradio.live/file=/content/drive/MyDrive/Fooocus/outputs/2024-06-15/log.html"

st.write(f'Here is the link to the Gradio app: {url}')

if generate_button:
    if prompt:
        dictionary = send_prompt(url,prompt, json_link, headless=headless) 
    for key, value in dictionary.items():
        if key == 'image':
            st.image(value, caption='Generated Image')
        else:
            st.write(value)
    else:
        st.write("Please enter a prompt.")
