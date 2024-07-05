from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import streamlit as st
import os
import stat

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_to_chrome_driver = os.path.join(BASE_DIR, 'chromedriver.exe')

# Set executable permissions for chromedriver.exe
if os.path.exists(path_to_chrome_driver):
    st.write(f"'chromedriver.exe' found at: {path_to_chrome_driver}")
    try:
        # Set the execute permission for the owner
        os.chmod(path_to_chrome_driver, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
        st.write(f"Executable: {os.access(path_to_chrome_driver, os.X_OK)}")
    except Exception as e:
        st.error(f"Failed to set executable permissions for 'chromedriver.exe': {str(e)}")
else:
    st.error(f"'chromedriver.exe' not found at: {path_to_chrome_driver}")

def download_pdf_using_selenium(url, dir):
    print(f"This is dir in function download pdf using selenium ! :- {dir}")
    st.write(f"This is dir in function download pdf using selenium ! :- {dir}")
    st.write(f"url is :- {url} And it will get saved in {dir}.")
    try:
        # Set up Chrome options to enable PDF download
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {
            "download.default_directory": dir,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        })

        # Set up the Chrome driver
        service = Service(path_to_chrome_driver)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the URL
        driver.get(url)

        # Close the browser
        driver.quit()
        print("PDF downloaded successfully!")

    except FileNotFoundError:
        st.error("Error: ChromeDriver executable not found. Please ensure 'chromedriver.exe' is in the correct location.")
    except webdriver.common.exceptions.WebDriverException as e:
        if "cannot find Chrome binary" in str(e):
            st.error("Error: Chrome browser not found. Please ensure Chrome is installed on your system.")
        else:
            st.error(f"WebDriver error: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
    st.write(f"Exiting the function download_pdf_using_selenium.")

if st.button("Download files"):
    st.write(BASE_DIR)
    output_dir = os.path.join(BASE_DIR, 'Input')
    st.write(output_dir)
    links = ['https://link.springer.com/content/pdf/10.1007/s00167-018-4953-z.pdf', 'https://lirias.kuleuven.be/retrieve/607878', 'https://journals.sagepub.com/doi/pdf/10.1177/19417381221087246']
    for link in links:
        download_pdf_using_selenium(link, output_dir)
