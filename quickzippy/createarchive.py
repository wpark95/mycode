#!/usr/bin/env python3

""" Zip It """

import os
import zipfile

# function to search for all files within a directory, and add them to our ZIP
def zipdir(dirpath, zipfileobj):
    
    """does the work of writing data into our zipfile"""
    # os.walk() returns a 3-tuple
    # thats a fancy way of saying it returns 3 things
    # always in the order... root, dirs, files
    # so the following line says given that you will return to us roots, dirs and files...
    for root, dirs, files in os.walk(dirpath):
        
        for file in files:  # we only want to loop across the file component
            
            print(os.path.join(root,file))   # create an aboslute path of where file lives
            
            zipfileobj.write(os.path.join(root, file)) ## adds files to our zipfileobject that was passed in
    
    return None # when we are done, no need to return any value

def main():

    # user input for the directory to be archived
    dirpath = input("What directory are we archiving today? ")

    # if the directory exists, then we can begin archiving it
    if os.path.isdir(dirpath):
        
        zippedfn = input("What should we call the finished archive file? ")

        # zippedfn is the zipped file for the archive
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:

            # create a zip file obj
            zipdir(dirpath, zipfileobj)

    # if the user input directory is invalid
    else:
        
        print ("Please run the script again with a valid directory to zip.")

main()
