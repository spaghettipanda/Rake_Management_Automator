# %%
import os
# %%
import ctypes
import time
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmsg
import tkinter.font as font

# Message Box
def message_box(type, message, title):
    try:
        root = Tk()
        root.withdraw()

        # Yes/No/Cancel Box
        if(type=='Y/N/C'):
            print(message)
            user_input = tkmsg.askyesnocancel(title, message)
            if(user_input==True):
                print(message + ': Yes')
                return True
            elif(user_input==False):
                print(message + ': No')
                return False
            elif(user_input==None):
                print(message + ': Cancel')
                return None
            else:
                raise ValueError('Unknown User Input! ', user_input)
                

        # Yes/No Box  
        elif(type=='Y/N'):
            user_input = tkmsg.askyesno(title, message)
            if(user_input==True):
                print(message + ': Yes')
                return True
            elif(user_input==False):
                print(message + ': No')
                return False
            else:
                raise ValueError('Unknown User Input! ', user_input)
        

        # OK/Cancel Box  
        elif(type=='O/C'):
            user_input = tkmsg.askokcancel(title, message)
            if(user_input==True):
                print(message + ': OK')
                return True
            elif(user_input==False):
                print(message + ': Cancel')
                return None
            else:
                raise ValueError('Unknown User Input! ', user_input)
        
        # OK
        elif(type=='O'):
            user_input = tkmsg.showinfo(title, message)
            if(user_input=='ok'):
                print(message + ': OK')
                return True
            else:
                raise ValueError('Unknown User Input! ', message + ': ' + user_input)
            
        elif(type=='warning'):
            tkmsg.showwarning(title, message)
            print(f'\n[Warning Box] \n{message}\n')
            
        elif(type=='error'):
            tkmsg.showerror(title, message)
            print(f'\n[Error Box] \n{message}\n')
            
        else:
            raise ValueError('Unknown MessageBox Type Selected: ', type)
        

    except ValueError as err:
        print(err.args)

def create_folder(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        open_folder(dir)

def open_folder(dir):
    os.startfile(dir)