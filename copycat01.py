#!/usr/bin/env python3

""" This script copies files and directories """

# import additional code to complete our task
import shutil
import os

def main(): 

    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # the following line will delete the directory if it exists already
    os.system("rm -rf /home/student/mycode/5g_research_backup/")

    # The following line will create the directory if it does not exist already
    # copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
