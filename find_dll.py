import os
def find_dll(dll_name, search_path):
    for root, dirs, files in os.walk(search_path):
            if dll_name in files:
                return os.path.join(root, dll_name)
    return None

dll_name = 'windivert.dll'
search_path = 'C:\\'

dll_path = find_dll(dll_name, search_path)

if dll_path:
     print(f'Found {dll_name} at: {dll_path}')
else:
     print(f'{dll_name} not found')