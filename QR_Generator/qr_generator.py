import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    st.title('QR Generator')

    st.sidebar.header('Input Options')
    input_option = st.sidebar.radio("Choose Input Option:", ('Manual Input', 'Upload .txt File', 'URL/Link'))

    if input_option == 'Manual Input':
        input_text = st.text_area("Enter text to generate QR code")

    elif input_option == 'Upload .txt File':
        uploaded_file = st.file_uploader("Upload .txt file", type=['txt'])
        if uploaded_file is not None:
            content = uploaded_file.getvalue().decode("utf-8")
            input_text = st.text_area("Uploaded Text", content)

    elif input_option == 'URL/Link':
        url = st.text_input("Enter URL/link")
        if url:
            input_text = url

    if st.button("Generate"):
        if input_text:
            qr_img = generate_qr(input_text)
            img_bytes = BytesIO()
            qr_img.save(img_bytes, format='PNG')
            img_bytes.seek(0)

            # Convert PIL Image to PNG format string
            img_str = img_bytes.getvalue()

            # Display the QR code using st.image()
            st.image(img_str, caption='Generated QR Code', use_column_width=True)

            # Download Button
            st.download_button(label="Download QR Code", data=img_str, file_name='generated_qr.png', mime='image/png')

if __name__ == '__main__':
    main()
