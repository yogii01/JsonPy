import json
import zipfile
import os

with open('main.json','r') as filesdata:
    filedata=json.load(filesdata)
    
files = filter( lambda x: os.path.isfile(os.path.join(filedata['path'], x)),
                        os.listdir(filedata['path']))

files = sorted( files,

                key = lambda x: os.path.getmtime(os.path.join(filedata['path'], x)))

fileno=filedata['files']
files.reverse()
print("The Update Files are:")

for file in files[5:]:
    os.remove(os.path.join(filedata['path'],file))
for file in files[:5]:
    file_path = os.path.join(filedata['path'],file)
    print(file)            


path=filedata['path']
def prepare_zip(path):
    new_file = filedata['path']+'.zip'
            
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
            
    for dir_file, dir_names, files in os.walk(filedata['path']):
        f_path = dir_file.replace(dir_file, '')
        f_path = f_path and f_path + os.sep
                
        for file in files:
            zip.write(os.path.join(filedata['path'], file), f_path + file)
    zip.close()
    os.rename(new_file,filedata['Zip_file_name'])
prepare_zip(filedata['path'])

  
