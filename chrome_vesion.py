import streamlit as st
import subprocess
import platform


def get_chrome_version():
    print(f"*"*100)
    st.info(f"*"*100)
    try:
        result = subprocess.run(['chrome', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        print(f"chrome version result is :- {result},\\version is {version}")
        st.info(f"chrome version result is :- {result},\\version is {version}")
        return version
    except Exception as e:
        return str(e)


def get_chromedriver_version() -> str:
    try:
        result = subprocess.run(['chromedriver', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        # print(result, '\\n', version)
        return version
    except Exception as e:
        return str(e)


def get_chromedriver_path():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(['where', 'chromedriver'], capture_output=True, text=True, check=True)
        else:
            result = subprocess.run(['which', 'chromedriver'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "ChromeDriver not found in PATH. Please check the installation."
    except Exception as e:
        return f"Error finding ChromeDriver: {str(e)}"


if st.button("Check The Chrome Version"):
    st.title('Chrome and ChromeDriver Versions')
    st.info(f"Hello World !")
    chrome_version = get_chrome_version()
    chromedriver_version = get_chromedriver_version()
    chromedriver_path = get_chromedriver_path()

    st.write(f'Chrome Version: {chrome_version}')
    st.write(f'ChromeDriver Version: {chromedriver_version}')
    st.write(f'ChromeDriver Path: {chromedriver_path}')
