from zipfile import ZipFile

filepath = r'C:\Users\admin\data.zip'

with ZipFile(filepath,'r') as zip:
    zip.printdir()
    zip.extractall()