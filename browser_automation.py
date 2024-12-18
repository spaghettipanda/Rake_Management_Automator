# %%
# pip install selenium-wire

from seleniumwire import webdriver
from selenium.webdriver.edge.options import Options

import time
import os
import shutil

# Download files from the URL
def download_url(url):
    print('Download URL: ', url)

    # Create folder 'tempdata' to store RVC csv files
    script_dir = os.path.join(os.getcwd(),'tempdata')
    download_dir = script_dir
    
    print('download_dir: ', download_dir)
    #capabilities = DesiredCapabilities().EDGE

    prefs = {'download.default_directory':download_dir,
             'download.prompt_for_download':False,
             'download.directory_upgrade':True,}

    # Remove unecessary pop ups and error logs
    edge_options = Options()
    edge_options.add_experimental_option('prefs', prefs)
    edge_options.add_argument('headless')
    edge_options.add_argument('log-level=3')
    
    driver = webdriver.Edge(options=edge_options)
    retry = True

    safety_counter = 0
    code = '0'

    while retry:
        if(safety_counter>10):
            print("Retry limit reached, cancelling download...")
            return code
        
        driver.get(url)
        print('...')

        # Access requests via the 'requests' attribute
        for request in driver.requests:
            if request.response and request.url == url:
                
                # Repeat process until successful status code 200
                code = request.response.status_code
                
                if request.response.status_code == 200:
                    retry=False # Stop retrying once successful
                    time.sleep(1)
                    
                    print(
                        'Response Code: ', 
                        request.response.status_code
                    )
                    
                    print('Download Successful ------------------\n')
            
            if not retry:
                driver.close()
                break
        
        safety_counter = safety_counter+1

# Delete tempfolder
def delete_folder(dir):
    shutil.rmtree(dir)

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