from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_to_chrome_driver = os.path.join(BASE_DIR, 'chromedriver.exe')


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
    st.write(f"Existing the function download_pdf_using_selenium.")


if st.button("download files"):
    print(BASE_DIR)
    output_dir = os.path.join(BASE_DIR, 'Input')
    print(output_dir)
    # links = ['https://link.springer.com/content/pdf/10.1007/s00167-018-4953-z.pdf', 'https://lirias.kuleuven.be/retrieve/607878', 'https://journals.sagepub.com/doi/pdf/10.1177/19417381221087246', 'https://journals.sagepub.com/doi/pdf/10.1177/2473011419846943', 'https://www.researchgate.net/profile/Kristoffer-Barfod/publication/275047988_Higher_rate_of_compensation_after_surgical_treatment_versus_conservative_treatment_for_acute_Achilles_tendon_rupture/links/56b40e5908ae61c480581924/Higher-rate-of-compensation-after-surgical-treatment-versus-conservative-treatment-for-acute-Achilles-tendon-rupture.pdf?_sg%5B0%5D=started_experiment_milestone&origin=journalDetail', 'https://journals.sagepub.com/doi/pdf/10.1177/2325967120909918', 'https://journals.sagepub.com/doi/pdf/10.1007/s11420-019-09684-0']
    links = ['https://link.springer.com/content/pdf/10.1007/s00167-018-4953-z.pdf', 'https://lirias.kuleuven.be/retrieve/607878', 'https://journals.sagepub.com/doi/pdf/10.1177/19417381221087246']
    for link in links:
        download_pdf_using_selenium(link, output_dir)