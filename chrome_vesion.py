import streamlit as st
from selenium import webdriver


def get_chrome_version():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Optional: Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    version = driver.capabilities['browserVersion']
    driver.quit()
    return version


def get_chromedriver_version():
    from selenium import __version__ as selenium_version
    return selenium_version


st.title('Chrome and ChromeDriver Versions')

chrome_version = get_chrome_version()
chromedriver_version = get_chromedriver_version()

st.write(f'Chrome Version: {chrome_version}')
st.write(f'ChromeDriver Version: {chromedriver_version}')
