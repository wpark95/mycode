#!/usr/bin/python3
""" Transform data between JSON, CSV, and Excel | Will """

import pandas

def main():

    print("Please enter the file name that you'd like to transform. Make sure to include file type (e.g., .json, .csv, etc.)")

    target_file = input(">>>")

    target_type = target_file.split(".")[-1]

    print("Please enter the file name and type that you'd like to save as (e.g., example.csv)")

    save_as = input(">>>")

    save_type = save_as.split(".")[-1]

    df = None

    # read

    if target_type == "json":

        df = pandas.read_json(target_file)

    if target_type == "csv":

        df = pandas.read_csv(target_file)

    if target_type == "xsl":

        df = pandas.read_excel(target_file)

    # write

    if save_type == "json":

        df.to_json(save_as)

    if save_type == "csv":

        df.to_csv(save_as)

    if save_type == "xsl":

        df.to_excel(save_as)

if __name__ == "__main__":
    main()
    
