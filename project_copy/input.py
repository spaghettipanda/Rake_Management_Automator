# %%
import sys

# Check if script should proceed
def proceed_input():
    user_input = ''
    user_input = input('Proceed? ')
    if (user_input == 'no' or user_input == 'No' or user_input == 'NO' or user_input == 'n' or user_input == 'N' or user_input == 'nO'):
        print('\n[' + user_input + '] was entered.\n')
        print('Cancelling execution...')
        print('--------------------------------------\n')
        sys.exit()
    else:
        if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y' or user_input == 'YES'):
            print('\n[' + user_input + '] was entered.\n')
            return True
        else:
            print('\n[' + user_input + '] was entered.\n')
            return False
        
# Check if script should exit
def exit_input():
    user_input = ''
    user_input = input('Execution Complete. Exit? ')
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y' or user_input == 'YES'):
        print('\n[' + user_input + '] was entered.\n')
        return True
    else:
        print('\n[' + user_input + '] was entered.\n')
        return False