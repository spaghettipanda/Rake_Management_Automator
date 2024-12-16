# %%
import sys

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
print('\n--------------------------------------\n')
print(shift)

# Work Order Required?
required = is_required(day_or_night_shift, weekend_status)
print(f'After Business Hours: {required}')
print('\n--------------------------------------\n')
valid_input = False
while(valid_input == False):
    valid_input = proceed_input()
    if(valid_input == False):
        print('\nPlease a valid input! [Yes/No/Y/N]')
        print('--------------------------------------\n')
    else:
        print('Proceeding with execution...')

# Check if tempdata already exists in directory    
if(tempdata_exists()):
  print('\n--------------------------------------')
  print('\"tempdata\" folder already exists... deleting existing folder...')
  delete_tempfolder()

# Download Cycle Point Data
print('\n--------------------------------------\n')
print('Downloading Cycle Point events from RVC...')
cycle_points = download_url('https://rsb.bhp.com/rvc/Application/ExportCsv?eventsEnum=CyclePoints')
# Download Car Count Data
print('Downloading Car Count events from RVC...')
car_counts = download_url('https://rsb.bhp.com/rvc/Application/ExportCsv/CarCounts?eventsEnum=CarCounts')

# Process Cycle Point Data
print('\n--------------------------------------\n')
print('Processing Cycle Point event data...')
cycle_points = read_csv('tempdata\RVC.csv')
print('Cleaning Cycle Point event data...')
cycle_points = clean_table(drop_noted(cycle_points))
cycle_points_html = convert_to_html(cycle_points)

# Process Car Count Data
print('\n--------------------------------------\n')
print('Processing Car Count event data...')
car_counts = read_csv('tempdata\RVC (1).csv')
print('Cleaning Car Count event data...')
car_counts = clean_table(drop_noted(car_counts))
car_counts_html = convert_to_html(car_counts)

# Delete Downloaded CSV Files
print('\n--------------------------------------\n')
print('Deleting temporary data...')
delete_tempfolder()

# Generate email as a pop up ready to send
print('\n--------------------------------------\n')
print('Generating email...')
generate_email(cycle_points_html, car_counts_html)

# Prepare program exit
valid_input = False
while(valid_input == False):
    valid_input = exit_input()
    if(valid_input == True):
        print('Exiting...')
        sys.exit()
    else:
        print('Simply close this window or Confirm program exit with [Yes/Y]: ')