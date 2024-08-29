import os
from playsound import playsound 
 
current_folder = os.getcwd()
print(f'Current folder: {current_folder}')

full_path = os.path.join(current_folder, 'results')
print(f'Full path: {full_path}')

file_name = os.path.join(full_path, 'test.mp3')
print(f'File name {file_name} File existance: {os.path.exists(file_name)}')

# Play the sound file 
playsound(file_name) 