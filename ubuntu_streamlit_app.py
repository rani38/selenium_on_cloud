import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from chrome_vesion import get_chromedriver_path

# Determine the absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'Input')

# Use a temporary directory for downloads
st.write(f"Temporary directory for downloads: {INPUT_DIR}")

# Update the path to ChromeDriver (without .exe)
path_to_chrome_driver = get_chromedriver_path()
st.info(f"Chrome Driver Path is:- {path_to_chrome_driver}")

st.write(f"ChromeDriver path: {path_to_chrome_driver}")


def download_pdf_using_selenium(url, dir):
    st.write(f"Attempting to download PDF from: {url}")
    st.write(f"Download directory: {dir}")

    try:
        # Set up Chrome options to enable PDF download
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {
            "download.default_directory": dir,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        })
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Set up the Chrome driver
        service = Service(path_to_chrome_driver)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the URL
        driver.get(url)

        # Wait for the download to complete
        time.sleep(1)

        # Close the browser
        driver.quit()
        print("PDF downloaded successfully!")

    except FileNotFoundError:
        print("Error: ChromeDriver executable not found. Please ensure 'chromedriver' is in the correct location.")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if st.button("Download files"):
    links = [
        'https://link.springer.com/content/pdf/10.1007/s00167-018-4953-z.pdf',
        'https://lirias.kuleuven.be/retrieve/607878',
        'https://journals.sagepub.com/doi/pdf/10.1177/19417381221087246'
    ]
    for link in links:
        download_pdf_using_selenium(link, INPUT_DIR)

    st.write("Download attempts completed. Check the logs for details.")