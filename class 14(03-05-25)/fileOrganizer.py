import os
import shutil
from datetime import datetime


# that is the source directory where i want to oraganise my files.
source_dir = "E:\\Cv Formate"

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename) # this line of code create a path name like that E:\Cv Formate\cv.docx

    if os.path.isdir(file_path):
        continue
    # if it's directary then continiue to next line of code
    
    # Create folder name 
    file_ext = filename.split('.')[-1]
    folder_name = os.path.join(source_dir, file_ext)

    os.makedirs(folder_name, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a new filename with the timestamp
    name_part = ".".join(filename.split('.')[:-1])
    new_filename = f"{name_part}_{timestamp}.{file_ext}"
    new_path = os.path.join(folder_name, new_filename)

    # Move and rename the file
    shutil.move(file_path, new_path)

print("Files organized and renamed successfully.")



'''
Noor code 

'''

# import os
# import shutil
# from datetime import datetime

# def organize(directory):
    
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         print(file_path)
        
#         if os.path.isdir(file_path):
#             continue
            
#         name_part, file_ext = os.path.splitext(filename)
#         file_ext = file_ext.lower() 
        
#         if not file_ext:
#             continue
            
#         folder_name = file_ext[1:] + "_files"
#         folder_path = os.path.join(directory, folder_name)
        
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)
            
#         current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
#         base_name = name_part
#         new_filename = f"{base_name}_{current_time}{file_ext}"
#         new_file_path = os.path.join(folder_path, new_filename)
        
#         try:
#             shutil.move(file_path, new_file_path)
#             print(f"Moved: {filename} -> {os.path.join(folder_name, new_filename)}")
#         except Exception as e:
#             print(f"Error moving {filename}: {e}")


    
# target_directory = input("Enter directory path to organize (or press Enter for current directory): ").strip()
    
# if not target_directory:
#     target_directory = os.getcwd()
    
# if os.path.isdir(target_directory):
#     print(f"Organizing files in: {target_directory}")
#     organize(target_directory)
#     print("Organization complete!")
# else:
#     print("Error: The specified directory does not exist.")