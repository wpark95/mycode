#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Using pandas to create new csv file with certain values"""

import pandas

def main():

    #create a dataframe called superdf from our csv data
    superdf = pandas.read_csv("superbirthday.csv")

    with open("superheroes.csv", "w") as new_csv:
        for row in superdf.to_dict(orient="records"):
            new_csv.write(f"{row['name']},{row['birthday month']}\n")

    # print the total number of lines (span returns (lines, columns))
    print(f"Total lines processed {superdf.shape[0]}")

if __name__ == "__main__":
    main()
