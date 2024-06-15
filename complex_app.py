# import necesary module 

from openai import OpenAI
from PIL import Image 
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel

# Initialize your image generation client

client = OpenAI(api_key = apikey)

single_img=dict(
        title="example",
        text="example",
        interval=None,
        img="Put the location image here!!!",             
)
    

def generate_images(image_description, num_images):
    image_gallery=[]
    for i in range(num_images):
        img_response=client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = img_response.data[0].url
        new_image= single_img.copy()
        new_image["tittle"]=f"Image {i+1}"
        new_images["text"]= image_description
        new_image["img"]= img_url
        image_gallery.append(new_image)
    return image_gallery

st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera:", layout="wide")

# create a title

st.title("Dalle-Image-Generation Tool")

# create a subheader

st.subheader("POWERED BY World's Most POWERFUL Image Generarion API- DALL-E")
img_description = st.text_input("Enter a description for image you want to generate")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=5, value= 1)

# create a button

if st.button("Generate Images"):
    
# generate_image=generate_images(img_description, num_of_images)
    
    carousel(items=generate_image, width=1)
    
    
