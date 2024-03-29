import streamlit as st
from pytube import YouTube

# Function to download YouTube video
def download_video(url, quality):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4', res=quality).first()
        stream.download()
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"Error occurred: {e}")

# Streamlit app UI
def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube URL
    video_url = st.text_input("Enter YouTube Video URL")

    # Select quality
    quality_options = ["360p", "480p", "720p", "1080p"]
    selected_quality = st.selectbox("Select Video Quality", quality_options)

    # Download button
    if st.button("Download"):
        if video_url == "":
            st.warning("Please enter a YouTube video URL.")
        else:
            download_video(video_url, selected_quality)

if __name__ == "__main__":
    main()
