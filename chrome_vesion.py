import streamlit as st
import subprocess


def get_chrome_version():
    try:
        result = subprocess.run(['chromium', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        return version
    except Exception as e:
        return str(e)


def get_chromedriver_version() -> str:
    try:
        result = subprocess.run(['chromedriver', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        return version
    except Exception as e:
        return str(e)


if st.button("Check The Chrome Version"):
    st.title('Chrome and ChromeDriver Versions')

    chrome_version = get_chrome_version()
    chromedriver_version = get_chromedriver_version()

    st.write(f'Chrome Version: {chrome_version}')
    st.write(f'ChromeDriver Version: {chromedriver_version}')
