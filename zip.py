 
import os
import zipfile
import datetime
 
def retrieve_file_paths(dirName):

 
  # setting file paths variable
  filePaths = []
   
  # Reading file from current directory
  for root,files in os.walk(dirName):
    for filename in files:
        # Creating filepath
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  return filePaths
 
 
def zip_file():
  current_date = datetime.datetime.now()

  #path of file to be zipped
  dir_name = 'html'
  filePaths = retrieve_file_paths('pictures')
   

  # creating zipfile
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    # zipping files one at a time
    for file in filePaths:
      zip_file.write(file)
    
    #adding html report
    zip_file.write('./html_report.html')
       
  print(f'[{current_date.strftime("%H:%M:%S")}] [INFO] {dir_name}.zip file is created successfully!')
   
