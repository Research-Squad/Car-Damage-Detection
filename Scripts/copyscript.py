import os, shutil

# first get the local path of the folder
localpath = str(os.getcwd())

# second we need to get the damage folder which will be the destination folder
damage = str(localpath + "/damage")

# then we get the input folder which is our root of all loops
inputpath = localpath + "/input"
outputpath = localpath + "/output"


# this list will contain all names of each file in each directory but only files that are .jpg or .json and are not tread_data -> look at line 70
filenames = []
# this list contains all path from the first instance instance
resultfirstdir = []
# this list contains all paths from the second instance
resultseconddir = []
# this list contains all paths from the third instance
resultthirddir = []

# go trough each file in the directory
for firstdir in os.listdir(inputpath):
    # check if the file is a directory
    if os.path.isdir(os.path.join(os.path.abspath(inputpath), firstdir)):
        # add it to next instance if its a directory
        resultfirstdir.append(os.path.join(os.path.abspath(inputpath), firstdir))
      

# go through each path in first instance
for secondly in resultfirstdir:
    # go trough each file in the directory
    for seconddir in os.listdir(str(secondly)):
        # check if the file is a directory
        if os.path.isdir(os.path.join(os.path.abspath(secondly), seconddir)):
            # add it to next instance if its a directory
            resultseconddir.append(os.path.join(os.path.abspath(secondly), seconddir))

# go through each path in second instance
for thirdly in resultseconddir:
    # go trough each file in the directory
    for thirddir in os.listdir(str(thirdly)):
        # check if the file is a directory
        if os.path.isdir(os.path.join(os.path.abspath(thirdly), thirddir)):
             # add it to next instance if its a directory
            resultthirddir.append(os.path.join(os.path.abspath(thirdly), thirddir))


# go through each path in third instance
for dire in resultthirddir:
    for file in os.listdir(dire):
        
        # get name an instance of file
        name, ext = os.path.splitext(file)

        # check if the name already exists in the list filenames and if not add it see line 72
        if name in filenames:
            # check if file exists in damage directory
            if file not in os.listdir(damage):
                print("copied files:")
                print(file)

                copyname, copyext = os.path.splitext(file)
                
                # copy both the json and jpg
                shutil.copy(os.path.join(os.path.abspath(dire), copyname) + '.json', damage)
                shutil.copy(os.path.join(os.path.abspath(dire), copyname) + '.jpg', damage)

        else:
            # only add if the ext is jpg or json and the name not tread_data
            if ext == ".jpg" or ext == ".json":
                if name != "tread_data":
                    filenames.append(name)

# MIT License
# Author: Ludwig von Schoenfeldt
    
