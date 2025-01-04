# When using PyInstaller, selenium-wire needs to be imported as a hook
# Also, certificates need to be added i.e. PyInstaller --add-data '.venv\path\to\ca.crt;seleniumwire' -- add data '.venv\path\to\ca.key;seleniumwire' --onefile etc
import sys

# Custom Modules
from shift_calc import *
from interface_input import *
from browser_automation import *
from csv_processing import *
from outlook_email_automation import *

try:

    # Current Shift
    # Set/Get current datetime
    now = get_now()

    # Get Shift details as a string
    day_of_week = get_day_of_week(now)
    today_date = get_date(now)
    weekend_status = get_weekend_status(now)
    day_or_night_shift = get_day_or_night_shift(now)
    now_time = convert_to_time(now)
    shift = f'Day: {day_of_week} \nDate: {today_date} \nTime: {now_time} \nShift: {weekend_status} {day_or_night_shift}'

    print('Starting script...')
    
    print('\n======================================\n')
    print('Press CTRL+C to cancel the script at any time')
    print('\n======================================\n')

    # User Confirmation
    proceed = message_box('Y/N', shift + '\n\nProceed with Execution?', 'REVIEW RAIL DATA WAIO')
    if(proceed==False):
        input('\nExecution cancelled. \n\nPress enter to close this window...')
        sys.exit()

    # Check if tempdata already exists in directory    
    if(file_exists('tempdata')):
        print('tempdata folder exists...')
        delete_folder('tempdata')
        create_folder('tempdata')
    else:
        input_loop = True
        while(input_loop==True):
            create_folder('tempdata')
            if(file_exists('tempdata')):
                break
                
    go = message_box('O/C', 'Start RVC csv downloads?', 'Proceed?') 
    print()

    if(go == None):
        print('Cancelling...')
        exit()
    
    # Download Cycle Point Data
    print('\n======================================\n')
    print('Downloading Cycle Point events from RVC...')
    cycle_points = 'https://rsb.bhp.com/rvc/Application/ExportCsv?eventsEnum=CyclePoints'
    download_url(cycle_points)
    if(type(cycle_points)==int):
        raise ValueError('Could not obtain cycle point data from RVC', cycle_points)
    
    # Download Car Count Data
    print('Downloading Car Count events from RVC...')
    car_counts = 'https://rsb.bhp.com/rvc/Application/ExportCsv/CarCounts?eventsEnum=CarCounts'
    download_url(car_counts)
    if(car_counts==False):
        raise ValueError('Could not obtain car count data from RVC', car_counts)

    message_box('O', 'Download Successful', 'Success')

    # Check if file exists in tempdta   
    if(file_exists('\\tempdata\\RVC.csv')):
        print('RVC.csv exists...')
    else:
        input_loop = True
        while(input_loop==True):
            overwrite = message_box('O/C' ,'Couldn\'t find RVC.csv in \\tempdata\\...\n\nPlease export/download the cycle point data as RVC.csv into the \\tempdata\\ folder\n\nClick OK once complete, or Cancel to cancel the script...', 'RVC.csv doesn\'t exist!')
            if(overwrite==True):
                if(file_exists('\\tempdata\\RVC.csv')):
                    break
                else:
                    continue
            elif(overwrite==None):
                print('Cancelling...')
                exit()

    # Data cleaning    
    remove_noted = message_box('Y/N', 'Remove rows already containing notes?', 'Remove noted rows?')

    remove_notes_column = message_box('Y/N', 'Remove the Notes column?', 'Remove Notes column?')

    # Process Cycle Point Data
    print('\n--------------------------------------\n')
    print('Processing Cycle Point event data...\n')
    cycle_data_file_name = like_file_search('RVC.', 'tempdata')
    cycle_points = read_csv(f'tempdata\\{cycle_data_file_name}')
    print('Cleaning Cycle Point event data...')
    if(remove_noted == True):
        cycle_points = drop_noted(cycle_points)
    if(remove_notes_column == True):
        cycle_points = clean_table_remove_notes(cycle_points)
    else:
        cycle_points = clean_table_keep_notes(cycle_points)
    cycle_points_html = convert_to_html(cycle_points)

    # Check if file exists in tempdata
    if(file_exists('\\tempdata\\RVC (1).csv')):
        print('RVC.csv exists...')
    else:
        input_loop = True
        while(input_loop==True):
            overwrite = message_box('O/C' , 'Couldn\'t find RVC (1).csv in \\tempdata\\...\n\nPlease try manual export/download the car count data as RVC (1).csv into the \\tempdata\\ folder\n\nClick OK once complete, or Cancel to cancel the script...', 'RVC (1).csv doesn\'t exist!')
            if(overwrite==True):
                if(file_exists('\\tempdata\\RVC (1).csv')):
                    break
                else:
                    continue
            elif(overwrite==None):
                print('Cancelling...')
                exit()

    # Process Car Count Data
    print('\n--------------------------------------\n')
    print('Processing Car Count event data...')
    car_count_file_name = like_file_search('(1).', 'tempdata')
    car_counts = read_csv(f'tempdata\\{car_count_file_name}')
    print('Cleaning Car Count event data...\n')
    if(remove_noted == True):
        car_counts = drop_noted(car_counts)
    if(remove_notes_column == True):
        car_counts = clean_table_remove_notes(car_counts)
    else:
        car_counts = clean_table_keep_notes(car_counts)
    car_counts_html = convert_to_html(car_counts)

    # Delete Downloaded CSV Files
    print('\n======================================\n')
    print('Deleting temporary data...')
    delete_folder('tempdata')

    # Generate email as a pop up ready to send
    print('\n======================================\n')
    print('Generating email...')
    generate_email(cycle_points_html, car_counts_html)

    # Prepare program exit
    print('\n======================================\n')
    input('Execution finished. \n\nPress enter to close this window...')
    sys.exit()

except ValueError as err:
    print(err.args)
    sys.exit()

except KeyboardInterrupt as err:
    print(err.args)
    input('\n\nPress enter to close this window...')
    sys.exit()

except SystemExit as err:
    sys.exit()

except Exception as err:
    print (f'\nUnknown Exception!!\n\nFull Error: {err}')
    print (f'\n\n\n{err.args}')
    input('\n\nPress enter to close this window...')
    sys.exit()
