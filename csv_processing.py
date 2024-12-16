# %%
import pandas as pd
import os
import shutil

# Read CSV data into pandas data frame
def read_csv(location):
    df = pd.read_csv(location)
    return df

# Drop Rows containing Notes in Notes field from the data frame
def drop_noted(df):
    for index,row in df.iterrows():
        print('Processing row [' + str(index) + ']...')
        if(pd.notnull(df.loc[index, 'Notes'])):
            print('Row [', index, ']: ')
            print(row['Date Time'], row['Rake'], row['Event Details'], row['Notes'])
            print('Contains Notes... Dropping Row!...')
            df.drop([index], axis=0, inplace=True)
        else:
            print(row['Date Time'], row['Rake'], row['Event Details'], row['Notes'])
            print('Row [', index, '] has no notes... Keeping row...')
    return df

# Clean table by removing 'Notes" and 'Unnamed' columns
def clean_table_remove_notes(df):
    print('Cleaning table... Removing \'Notes\' and \'Unnamed column\'')
    df.drop('Notes', axis=1, inplace=True)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    return df

# Clean table by removing unused 'Unnamed' columns
def clean_table_keep_notes(df):
    print('Cleaning table... Removing \'Unnamed column\', Notes column retained.')
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    return df

# Convert the table to HTML format - Email Friendly!
def convert_to_html(df):
    df = df.to_html(index=False)
    return df

# Search for a file with name similar
def like_file_search(file_name, sub_path=None):
    path = f'{os.getcwd()}'
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file_name in file):
                return file
            
# Search for a file with name similar
def like_file_search(file_name, sub_path):
    path = f'{os.getcwd()}\\{sub_path}'
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file_name in file):
                return file

# Check if file already exists
def file_exists(file):
    file = f'\\{file}'
    print('\nChecking for file: ' + f'{file}')
    cwd = os.getcwd()

    path = cwd+file
    exists = os.path.exists(path)
    print(os.path)
    return(os.path.exists(path))

def path_join():
    return os.path.join()

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

