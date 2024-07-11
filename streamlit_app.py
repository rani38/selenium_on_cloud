import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from chrome_vesion import get_chromedriver_path, get_chrome_version, get_chromedriver_version
import time
from multiprocessing import Pool


# Determine the absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'Input', 'google_scholar', 'scholar_pdfs')

chrome_version = get_chrome_version()
chromedriver_version = get_chromedriver_version()
chromedriver_path = get_chromedriver_path()

st.write(f"Temporary directory for downloads: {INPUT_DIR}")
st.write(f'Chrome Version: {chrome_version}')
st.write(f'ChromeDriver Version: {chromedriver_version}')
st.write(f'ChromeDriver Path: {chromedriver_path}')


def download_pdf_using_selenium(url, dir):
    st.write(f"Attempting to download PDF from: {url}")
    st.write(f"Download directory: {dir}")

    if not os.path.exists(dir):
        os.makedirs(dir)
        st.write(f"Created directory: {dir}")

    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('prefs', {
            "download.default_directory": dir,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        })

        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(url)
        # time.sleep(10)  # Wait for download to start

        # Wait for download to complete (adjust timeout as needed)
        WebDriverWait(driver, 1).until(
            lambda x: any([filename.endswith(".pdf") for filename in os.listdir(dir)])
        )

        driver.quit()

        # Verify if a new PDF file was downloaded
        pdf_files = [f for f in os.listdir(dir) if f.endswith('.pdf')]
        if pdf_files:
            st.success(f"PDF downloaded successfully: {pdf_files[-1]}")
        else:
            st.warning("No PDF file found after download attempt.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    finally:
        if 'driver' in locals():
            driver.quit()


if st.button("Download files"):
    links = ['https://link.springer.com/content/pdf/10.1007/s00167-018-4953-z.pdf', 'https://journals.sagepub.com/doi/pdf/10.1007/s11420-019-09684-0', 'https://journals.sagepub.com/doi/pdf/10.1177/2325967120909918', 'https://gupea.ub.gu.se/bitstream/handle/2077/57423/gupea_2077_57423_4.pdf?sequence=4', 'https://link.springer.com/content/pdf/10.1007/s00167-018-4954-y.pdf', 'https://link.springer.com/content/pdf/10.1186/s40634-020-00277-z.pdf']
    start_time = time.time()
    # for link in links:
    #     download_pdf_using_selenium(link, INPUT_DIR)
    with Pool(processes=os.cpu_count()) as pool:
        pool.starmap(download_pdf_using_selenium, [(link, INPUT_DIR) for link in links])
    st.success(
        "Files have been successfully downloaded. You can navigate to 'Get Downloaded Articles' Options and download it.")

    end_time = time.time()
    st.write("Time taken:", end_time - start_time, "seconds")
