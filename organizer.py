import os
import shutil
from pathlib import Path

BASE_DIRECTORY = Path.home()/'Downloads'

folders = {
    'Images':BASE_DIRECTORY/'Images',
    'Videos':BASE_DIRECTORY/'Videos',
    'Docs':BASE_DIRECTORY/'Docs',
    'Others':BASE_DIRECTORY/'Others'
}

for folder in folders.values():
    folder.mkdir(exist_ok=True)
    
Images = ('.jpg','.jpeg','.png','.gif','.webp')
Videos = ('.mp4','.mov','.mkv','.webm','.flv','.wmv')
Docs = ('.pdf','.doc','.docx','.txt','.xlsx','.pptx')

def is_Images(file):
    return file.suffix.lower()in Images

def is_Videos(file):
    return file.suffix.lower()in Videos

def is_Docs(file):
    return file.suffix.lower()in Docs

for file in BASE_DIRECTORY.iterdir():
    if file.is_dir():
        continue

    if is_Images(file):
        shutil.move(str(file),str(folders['Images']/file.name))
        print('Moved top Images')

    elif is_Videos(file):
        shutil.move(str(file),str(folders['Videos']/file.name))
        print('Moved to Videos')

    elif is_Docs(file):
        shutil.move(str(file),str(folders['Docs']/file.name))
        print('Moved to Docs')

    else:
        shutil.move(str(file),str(folders['Others']/file.name))
        print('Moved to Others')

        print('File Organizer.')
        print('Done, files moved and organized.')


   

