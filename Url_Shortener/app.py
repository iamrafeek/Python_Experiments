import streamlit as st
import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

def main():
    st.title("URL Shortener")
    url = st.text_input("Enter the URL to shorten:")
    
    if st.button("Shorten"):
        if url:
            short_url = shorten_url(url)
            st.success(f"Shortened URL: {short_url}")
        else:
            st.error("Please enter a URL.")

if __name__ == "__main__":
    main()
