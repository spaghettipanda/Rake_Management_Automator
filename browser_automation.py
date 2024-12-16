# %%
# pip install selenium-wire
# pip install blinker==1.7.0

from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import shutil

# Download files from the URL
def download_url(url):
    print('Download URL: ', url)
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

    safety_counter = 0
    code = '0'

    while x:
        if(safety_counter>10):
            print("Retry limit reached, cancelling download...")
            return code

        driver.get(url)
        print('...')

        # Access requests via the `requests` attribute
        for request in driver.requests:
            if request.response and request.url == url:
                # Repeat process until successful status code 200
                code = request.response.status_code
                if request.response.status_code == 200:
                    x=False
                    time.sleep(1)
                    print(
                        'Response Code: ', 
                        request.response.status_code
                    )
                    print('Download Successful ------------------\n')
                    x=False
        if not x:
            driver.close()
            break
        safety_counter = safety_counter+1

# Delete tempfolder
def delete_tempfolder():
    shutil.rmtree('tempdata')

# Check if file already exists
def file_exists(file):
    file = f'\\{file}'
    print('\nChecking for file: ' + f'{file}')
    cwd = os.getcwd()

    path = cwd+file
    exists = os.path.exists(path)

    return(os.path.exists(path))

def path_join():
    return os.path.join()