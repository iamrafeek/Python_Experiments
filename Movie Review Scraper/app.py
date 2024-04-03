import streamlit as st
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def scrape_movie_reviews(movie_name):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()
    
    # Open Google in the browser
    driver.get("https://www.google.com")
    
    # Find the search box and enter the movie name
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(movie_name + " reviews")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tF2Cxc")))
    
    # Find and click the "More" button to expand the reviews section
    try:
        more_button = driver.find_element(By.XPATH, "//span[contains(text(), 'More audience reviews')]")
        more_button.click()
        time.sleep(2)  # Wait for the reviews section to expand
    except NoSuchElementException:
        st.write("More button not found.")
    
    # Find the review snippets in the search results
    reviews = []
    try:
        review_elements = driver.find_elements(By.XPATH, "//span[@jsname='pkrv7']")
        
        # Extract the review content
        for element in review_elements:
            review = element.text
            reviews.append(review)
    except NoSuchElementException:
        st.write("Reviews not found.")
    
    # Close the webdriver
    driver.quit()
    
    # Write the reviews to a CSV file with delimiter between each review
    file_name = movie_name.replace(" ", "_") + "_reviews.csv"  # Adjust the file name
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for review in reviews:
            writer.writerow(['-' * 40])  # Delimiter between reviews
            writer.writerow([review])

# Streamlit UI
st.title("Movie Review Scraper")

# Input field for movie name
movie_name = st.text_input("Enter the movie name:")

# Button to trigger scraping
if st.button("Scrape Reviews"):
    if movie_name:
        scrape_movie_reviews(movie_name)
        st.success(f"Reviews scraped successfully! Check '{movie_name}_reviews.csv'")
    else:
        st.warning("Please enter a movie name.")
