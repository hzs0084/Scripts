import os

# Define the username to name mapping with lowercase usernames
username_to_name = {
    "sza0188": "Sydni Adams", "baa0030": "Brent Adamson", "agb0069": "Ashlynn Bara",
    "aab0101": "Aiden Bare", "zcb0005": "Zack Bellamy","drb0052": "Daniel Blair","geb0051": "Greer Boland",
    "lkb0047": "Lily Bradford","dcb0069": "Dannon Buggs","amc0225": "Abby Camlic","rac0075": "Rebecca Chow-Wah",
    "rid0002": "Robert Davis","cbd0033": "Clay Doll","cve0003": "Cooper Evans","maf0078": "Morgan Fields",
    "kbg0022": "Kate Goggans","keg0084": "Kristin Guidry","jgh0045": "Julia Helms","lah0084": "Landon Holloway",
    "tkh0018": "Tyler Huff","pth0012": "Parker Hughes","msj0022": "Mary Sanders James","acj0060": "Anna Johnson",
    "gwj0003": "Grant Johnson","elk0031": "Ethel Kostmayer","wdk0010": "William Kurtz","cml0087": "Cameron Lewis",
    "elm0063": "Eryn Marshall","jrm0143": "Jackson May", "dpn0002": "DJ Newberry","mto0012": "Mary Tristen Osborn",
    "aco0020": "Audrey Osborne","mmp0083": "Morgan Parish","gnr0010": "Griffin Race","ddr0019": "Dylan Roper",
    "wes0025": "Ethan Schuch","les0109": "Lauren Short","ams0243":"Austin Smith","jms0241": "Joe Sport",
    "jmw0219": "Jacob Waters","maw0163": "Madison Williams","afw0031": "Abby Wright"
}

# Directory where you want to rename the folders
target_directory = r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions\PA 4'

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
