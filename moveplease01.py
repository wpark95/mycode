#!/usr/bin/env python3


""" This program creates a file, moves it to a different directory and renames it """

# import necessary modules
import shutil
import os

def main():
    
    # force the Python program to start in the home user directory
    os.chdir("/home/student/mycode/")

    # move file at the path source to the path destination
    shutil.move("raynor.obj", "ceph_storage/")

    # prompt the user for a new name for the kerrigan.obj file
    xname = input("What is the new name for kerrigan.obj?")

    # rename the current kerrigan.obj file to be user input from earlier
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname + ".obj")

if __name__ == "__main__":
    main()

