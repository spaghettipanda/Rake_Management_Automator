# %%
# pip install selenium-wire
# pip install blinker==1.7.0

from seleniumwire import webdriver
from io import StringIO
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import shutil

# Download files from the URL
def download_url(url):
    # Create folder 'tempdata' to store RVC csv files
    script_dir = os.path.join(os.getcwd(),'tempdata')
    download_dir = script_dir

    capabilities = DesiredCapabilities().CHROME

    # Remove unecessary pop ups and error logs
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--log-level=3')

    prefs = {'download.default_directory':download_dir,
             'download.prompt_for_download':False,
             'download.directory_upgrade':True}

    chrome_options.add_experimental_option('prefs', prefs)
    capabilities.update(chrome_options.to_capabilities())

    driver = webdriver.Chrome(options=chrome_options)
    x= True
    while x:
        driver.get(url)

        # Access requests via the `requests` attribute
        for request in driver.requests:
            if request.response and request.url == url:
                print(
                    request.url,
                    request.response.status_code
                )
                # Repeat process until successful status code 200
                if request.response.status_code == 200:
                    x=False
                    time.sleep(1)
                    print('Success\n')
                    x=False
        if not x:
            driver.close()
            break

# Delete tempfolder
def delete_tempfolder():
    shutil.rmtree('tempdata')

# Check if tempfolder already exists
def tempdata_exists():
    return(os.path.exists('tempdata'))