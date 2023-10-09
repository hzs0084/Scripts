import os
import openpyxl

# Directory where you want to rename the folders
target_directory = r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions\PA 2'

# Load the Excel file
excel_file_path = r'C:\Users\hzs0084\Downloads\2023-09-16T1151_Grades-ISMN-3080-001_(Fall_2023).xlsx'

# Create an empty dictionary to store the username to name mapping
username_to_name = {}

# Open the Excel file
wb = openpyxl.load_workbook(excel_file_path)
ws = wb.active

# Iterate through rows starting from row 4 (A4 and D4)
for row in ws.iter_rows(min_row=4, max_col=4, values_only=True):
    name = row[0]  # Last name, first name format
    username = row[1]
    
    # Check if username is a string
    if isinstance(username, str):
        # Split the name into first name and last name
        last_name, first_name = name.split(', ')
        
        # Create the full name
        full_name = f"{first_name} {last_name}"
        
        # Store the mapping in lowercase
        username_to_name[username.lower()] = full_name

# Iterate through folders in the target directory
for foldername in os.listdir(target_directory):
    folder_path = os.path.join(target_directory, foldername)
    
    # Check if the lowercase version of the foldername is in the username mapping
    if foldername.lower() in username_to_name:
        new_name = username_to_name[foldername.lower()]
        new_folder_path = os.path.join(target_directory, new_name)
        
        # Rename the folder
        os.rename(folder_path, new_folder_path)
        print(f"Renamed folder '{foldername}' to '{new_name}'")

# Close the Excel file
wb.close()
