#!/usr/bin/python3
""" A simple program that creates a .txt file.| Will """

def main():
    """ Generates a .txt file when invoked """
    # create a file with the provided file name
    with open ("test.txt", "w") as created_file:
        # write a line that informs the user that this is the file that's been created
        created_file.write("This is the file that you created.")

if __name__ == "__main__":
    main()
