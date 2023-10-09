import os

#Creates the lab folder for me in the file path

path= r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions'

os.chdir(path)

lab3Folder = 'PA 2' #Update the string to reflect the name of the folder
if not os.path.exists(lab3Folder):      #Update the path as well otherwise the Path won't exist
    os.makedirs(lab3Folder)

#Creates the folders for students inside the Lab folder

path= r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions\Test 3' #put r in front of a normal string so that it can convert the string to a raw string

os.chdir(path)

classSet = {"Ashlynn Bara", "Sydni Adams", "Brent Adamson","Ashlynn Bara", "Aiden Bare", "Zack Bellamy",
            "Daniel Blair", "Greer Boland","Lily Bradford","Dannon Buggs", "Abby Camlic", "Rebecca Chow-Wah",
            "Robert Davis", "Clay Doll", "Cooper Evans", "Morgan Fields", "Kate Goggans", "Kristin Guidry",
            "Julia Helms", "Landon Holloway", "Tyler Huff", "Parker Hughes", "Mary Sanders James", "Anna Johnson",
            "Grant Johnson", "Ethel Kostmayer", "William Kurtz", "Cameron Lewis", "Eryn Marshall", "Jackson May", "DJ Newberry",
            "Mary Tristen Osborn", "Audrey Osborne", "Morgan Parish", "Griffin Race", "Dylan Roper", "Ethan Schuch", "Lauren Short",
            "Austin Smith", "Joe Sport", "Jacob Waters", "Madision Williams", "Abby Wright"}
for classFolder in classSet:
    if not os.path.exists(classFolder):
        os.makedirs(classFolder)

#Uncomment this line of code and run it onlt when you want to DELETE the parent folder
#path = r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions'
#os.rmdir(lab3Folder) 
    
#Look into making a piece of code that will extract the zip files and then put them in the respective folder for me
#Potential issues that I may face is assigning a path for each student, following the same naming convention, 
#Can I genereate an output of student code? Make grading easier for me?

print("I am finished!")


# Newfolder = 'Sydni Adams'
# if not os.path.exists(Newfolder):   #If the firectory already exists then it will skip
#     os.makedirs(Newfolder)
# Newfolder = 'Brent Adamson'
# if not os.path.exists(Newfolder):  
#     os.makedirs(Newfolder)

# #I could make a set or an array and then have the for loop go through that array and make folders

# Newfolder = 'Ashlynn Bara'      
# os.makedirs(Newfolder)


# Newfolder = 'Aiden Bare'      
# os.makedirs(Newfolder)


# Newfolder = 'Zack Bellamy'      
# os.makedirs(Newfolder)


# Newfolder = 'Daniel Blair'      
# os.makedirs(Newfolder)


# Newfolder = 'Greer Boland'      
# os.makedirs(Newfolder)


# Newfolder = 'Lily Bradford'      
# os.makedirs(Newfolder)


# Newfolder = 'Dannon Buggs'      
# os.makedirs(Newfolder)


# Newfolder = 'Abby Camlic'      
# os.makedirs(Newfolder)


# Newfolder = 'Rebecca Chow-Wah'      
# os.makedirs(Newfolder)


# Newfolder = 'Robert Davis'      
# os.makedirs(Newfolder)


# Newfolder = 'Clay Doll'      
# os.makedirs(Newfolder)


# Newfolder = 'Cooper Evans'      
# os.makedirs(Newfolder)


# Newfolder = 'Morgan Fields'      
# os.makedirs(Newfolder)


# Newfolder = 'Kate Goggans'      
# os.makedirs(Newfolder)


# Newfolder = 'Kristin Guidry'      
# os.makedirs(Newfolder)


# Newfolder = 'Julia Helms'      
# os.makedirs(Newfolder)


# Newfolder = 'Landon Holloway'      
# os.makedirs(Newfolder)


# Newfolder = 'Tyler Huff'      
# os.makedirs(Newfolder)


# Newfolder = 'Parker Hughes'      
# os.makedirs(Newfolder)


# Newfolder = 'Mary Sanders James'      
# os.makedirs(Newfolder)


# Newfolder = 'Anna Johnson'      
# os.makedirs(Newfolder)


# Newfolder = 'Grant Johnson'      
# os.makedirs(Newfolder)


# Newfolder = 'Ethel Kostmayer'      
# os.makedirs(Newfolder)


# Newfolder = 'William Kurtz'      
# os.makedirs(Newfolder)


# Newfolder = 'Cameron Lewis'      
# os.makedirs(Newfolder)


# Newfolder = 'Eryn Marshall'      
# os.makedirs(Newfolder)


# Newfolder = 'Jackson May'      
# os.makedirs(Newfolder)


# Newfolder = 'DJ Newberry'      
# os.makedirs(Newfolder)


# Newfolder = 'Mary Tristen Osborn'      
# os.makedirs(Newfolder)


# Newfolder = 'Audrey Osborne'      
# os.makedirs(Newfolder)


# Newfolder = 'Morgan Parish'      
# os.makedirs(Newfolder)


# Newfolder = 'Griffin Race'      
# os.makedirs(Newfolder)


# Newfolder = 'Dylan Roper'      
# os.makedirs(Newfolder)


# Newfolder = 'Ethan Schuch'      
# os.makedirs(Newfolder)


# Newfolder = 'Lauren Short'      
# os.makedirs(Newfolder)


# Newfolder = 'Austin Smith'      
# os.makedirs(Newfolder)


# Newfolder = 'Joe Sport'      
# os.makedirs(Newfolder)


# Newfolder = 'Jacob Waters'      
# os.makedirs(Newfolder)


# Newfolder = 'Madison Williams'      
# os.makedirs(Newfolder)


# Newfolder = 'Abby Wright'      
# os.makedirs(Newfolder)

# print('IT IS NOW DONE')