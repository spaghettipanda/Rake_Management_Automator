# %%
import selenium
import pandas as pd

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

# Clean table by removing unused 'Notes" and 'Unnamed' columns
def clean_table(df):
    print('Cleaning table... Removing \'Notes\' and \'Unnamed column\'')
    #dataframe.drop('Unnamed', axis=1, inplace=True)
    df.drop('Notes', axis=1, inplace=True)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    return df

# Convert the table to HTML format - Email Friendly!
def convert_to_html(df):
    df = df.to_html(index=False)
    return df