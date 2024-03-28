import streamlit as st
from PIL import Image
import numpy as np
import io
import base64

# Function to resize image while maintaining aspect ratio
def resize_image(image, width, height):
    aspect_ratio = image.width / image.height
    new_width = width
    new_height = int(new_width / aspect_ratio)
    if new_height > height:
        new_height = height
        new_width = int(new_height * aspect_ratio)
    return image.resize((new_width, new_height))

# Function to compress image to meet target file size
def compress_image(image, target_size):
    img_io = io.BytesIO()
    image.save(img_io, format='JPEG', quality=90)
    img_bytes = img_io.getvalue()
    
    while len(img_bytes) > target_size * 1024:
        img_io = io.BytesIO()
        image.save(img_io, format='JPEG', quality=90)
        img_bytes = img_io.getvalue()
        factor = np.sqrt((len(img_bytes) / (target_size * 1024)))
        width, height = image.size
        image = image.resize((int(width / factor), int(height / factor)))
    
    return image

def main():
    st.title("Image Format Converter")

    # Input parameters
    st.header("Input Parameters")
    uploaded_file = st.file_uploader("Upload Image:", type=["jpg", "jpeg", "png"])
    width = st.number_input("Width:", min_value=1, step=1, value=300)
    height = st.number_input("Height:", min_value=1, step=1, value=300)
    unit = st.selectbox("Unit:", ["pixels", "inches", "centimeters"])
    target_size = st.number_input("Target File Size (KB):", min_value=1, step=1, value=100)

    if st.button("Convert") and uploaded_file is not None:
        # Load original image
        image = Image.open(uploaded_file)

        # Convert unit to pixels
        if unit == "inches":
            width *= 96
            height *= 96
        elif unit == "centimeters":
            width *= 37.7952755906
            height *= 37.7952755906

        # Resize image
        resized_image = resize_image(image, width, height)

        # Compress image to meet target file size
        compressed_image = compress_image(resized_image, target_size)

        # Display converted image
        st.image(compressed_image, caption="Converted Image", use_column_width=True)

        # Save image
        buffered = io.BytesIO()
        compressed_image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()

        # Download button
        st.download_button("Download Image", img_bytes, file_name='converted_image.jpg')

if __name__ == "__main__":
    main()
