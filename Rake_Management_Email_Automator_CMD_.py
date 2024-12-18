# %%
import sys
import shutil

# Custom Modules
from shift_calc import *
from input import *
from csv_processing import *
from browser_automation import *
from outlook_email_automation import *

# Current Shift
# Set/Get current datetime
now = get_now()

# Get Shift details as a string
day_of_week = get_day_of_week(now)
today_date = get_date(now)
weekend_status = get_weekend_status(now)
day_or_night_shift = get_day_or_night_shift(now)
now_time = convert_to_time(now)
shift = f'{today_date}\n{day_of_week} {now_time}\n{weekend_status} {day_or_night_shift}'
print('\n======================================\n')
print(shift)

# User Confirmation
required = is_required(day_or_night_shift, weekend_status)
print(f'After Business Hours: {required}')
print('\n======================================\n')
print('Proceed?')
valid_input = None
while(valid_input != True):
    valid_input = std_input()
    if(valid_input == None):
        print('\nPlease a valid input! [Yes/No/Y/N]')
        print('--------------------------------------\n')
    elif(valid_input == True):
        print('Proceeding with execution...')
    elif(valid_input == False):
        print('Exiting...')
        sys.exit()

# Check if tempdata already exists in directory    
if(tempdata_exists()):
  print('\n======================================')
  print('\"tempdata\" folder already exists... deleting existing folder...')
  delete_tempfolder()

# Download Cycle Point Data
print('\n======================================\n')
print('Downloading Cycle Point events from RVC...')
cycle_points = download_url('https://rsb.bhp.com/rvc/Application/ExportCsv?eventsEnum=CyclePoints')
# Download Car Count Data
print('Downloading Car Count events from RVC...')
car_counts = download_url('https://rsb.bhp.com/rvc/Application/ExportCsv/CarCounts?eventsEnum=CarCounts')


# Data cleaning
print('======================================\n')
print('Do you want to REMOVE rows containing notes?')
clean_input = None
while(clean_input == None):
    clean_input = std_input()
    if(clean_input == None):
        print('\nPlease a valid input! [Yes/No/Y/N]')
        print('--------------------------------------\n')
    elif(clean_input == False):
        remove_rows_with_notes = False
        print('Remove Rows containing Notes: ' + str(remove_rows_with_notes))
    elif(clean_input == True):
        remove_rows_with_notes = True
        print('Remove Rows containing Notes: ' + str(remove_rows_with_notes))

print('\n======================================\n')
print('Do you want to REMOVE the notes column in the email?')
clean_input = None
while(clean_input == None):
    clean_input = std_input()
    if(clean_input == None):
        print('\nPlease a valid input! [Yes/No/Y/N]')
        print('--------------------------------------\n')
    elif(clean_input == False):
        remove_notes_column = False
        print('Remove Notes Column: ' + str(remove_notes_column))
    elif(clean_input == True):
        remove_notes_column = True
        print('Remove Notes Column: ' + str(remove_notes_column))
    else:
        print("Unknown Error: How did you get here?")



# Process Cycle Point Data
print('\n--------------------------------------\n')
print('Processing Cycle Point event data...\n')
cycle_points = read_csv('tempdata\RVC.csv')
print('Cleaning Cycle Point event data...')
if(remove_rows_with_notes == True):
    cycle_points = drop_noted(cycle_points)
if(remove_notes_column == True):
    cycle_points = clean_table_remove_notes(cycle_points)
else:
    cycle_points = clean_table_keep_notes(cycle_points)
cycle_points_html = convert_to_html(cycle_points)


# Process Car Count Data
print('\n--------------------------------------\n')
print('Processing Car Count event data...')
car_counts = read_csv('tempdata\RVC (1).csv')
print('Cleaning Car Count event data...\n')
if(remove_rows_with_notes == True):
    car_counts = drop_noted(car_counts)
if(remove_notes_column == True):
    car_counts = clean_table_remove_notes(car_counts)
else:
    car_counts = clean_table_keep_notes(car_counts)
car_counts_html = convert_to_html(car_counts)



# Delete Downloaded CSV Files
print('\n======================================\n')
print('Deleting temporary data...')
delete_tempfolder()

# Generate email as a pop up ready to send
print('\n======================================\n')
print('Generating email...')
#generate_email(cycle_points_html, car_counts_html)

# Prepare program exit
print('\n======================================\n')
print('Exit the script? (Alternatively, you can just close this window)')
valid_input = None
while(valid_input != True):
    valid_input = std_input()
    if(valid_input == None):
        print('\nPlease a valid input! [Yes/No/Y/N]')
        print('--------------------------------------\n')
    elif(valid_input == True):
        print('Exiting...')
        sys.exit()
    elif(valid_input == False):
        print('Exit?')