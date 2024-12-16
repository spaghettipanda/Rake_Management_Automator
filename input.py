# %%
import sys
        
# Standard input logic    
def std_input():
    user_input = ''
    user_input = input('[Y/N] ')
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y' or user_input == 'YES'):
        print('\n[' + user_input + '] was entered.\n')
        return True
    elif (user_input == 'no' or user_input == 'No' or user_input == 'NO' or user_input == 'n' or user_input == 'N' or user_input == 'nO'):
        print('\n[' + user_input + '] was entered.\n')
        return False
    else:
        print('\n[' + user_input + '] was entered.')
        return None