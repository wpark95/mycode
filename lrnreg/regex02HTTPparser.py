#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""
    
    user_command = " "

    while user_command != "q":

        print("Where should we search?")
        url = input("> ")  # collect user input

        print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
        searchFor = input("> ")

        resp = requests.get(url)  # Send HTTP GET
        searchMe = resp.text      # strip everything off the response as a string (text)

        # use the re.search() to determine if our website has the pattern we are looking for
        # it works by taking arguments, the first is the regex search pattern, and the second
        # is the string to search within

        if re.search(searchFor, searchMe):
            print("Found a match!")
            num_match = len(re.findall(searchFor, searchMe))
            print("Number of matches found: " + str(num_match)) 

        else:
            print("No match!")

        user_command = input("Would you like to keep searching? Hit enter to continue or enter q to quit")

if __name__ == "__main__":
    main()

