import requests
import os
import io
from PIL import Image
from datetime import datetime
import streamlit as st

HUGGINGFACEHUB_API_TOKEN = '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'


def text2image(prompt: str):
    API_URL = ( 
        'https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5'
        ) 
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payload = { 
        'inputs': prompt,
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes)) 
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S") 
    filename = os.path.join('output_images/'f"{timestamp}.jpg")
    image.save(filename)
    return filename
def main():
    st.set_page_config(page_title='Text2Image', page_icon='🖼️')

    # Set page config and title
    # Define custom CSS for animations, background image, and transitions
    st.markdown("""
        <style>
             /* Define animation for title */
            @keyframes titleAnimation {
                0% { transform: translateX(-100%); opacity: 0; }
                100% { transform: translateX(0); opacity: 1; }
            }

            /* Apply animation to title */
            .title-container {
                animation: titleAnimation 1s forwards;
            }
            /* Define animation for submit button */
            @keyframes buttonAnimation {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<h1 class="title-container">Text To Image Generator App!🖼️</h1>', unsafe_allow_html=True)
    # Display form to enter text prompt
    with st.form(key='my_form'):
        query = st.text_area(
            label="Enter text prompt for the image...",
            help="Enter a prompt for the image here...",
            key="query",
            max_chars=50,
        )
        submit_button = st.form_submit_button(label="Generate Image")

    # If query and submit button are clicked, generate image
    if query and submit_button:
        with st.spinner("Generating image in progress...please wait!"):
            # Generate image
            image_file = text2image(prompt=query)
            
            # Display generated image with caption
            st.subheader("       Here's your beautiful image 🖼️")
            st.image(f"./{image_file}", caption=query)

            # Show success message with animation
            st.success("Image generation complete! ✨")
    
if __name__ == "__main__":
    main()
