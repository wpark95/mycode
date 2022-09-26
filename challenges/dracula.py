#!/usr/bin/python3
""" Dracula counter  """

def main():

    #dracula counter
    counter = 0

    # open Dracula in read mode
    dracula_file = open("dracula.txt", "r")

    # open vampytimes in write mode
    vampytimes = open("vampytimes.txt", "w")

    # create a list of lines from Dracula
    draculist = dracula_file.readlines()

    # loop over lines
    for line in draculist:

        # print each line if the line contains the word vampire
        if "vampire" in line.lower():
            vampytimes.write(line)
            counter += 1

    # close the file
    dracula_file.close()

    vampytimes.close()
    
    # print the number of lines that has vampire
    print(counter)

if __name__ == "__main__":
    main()
