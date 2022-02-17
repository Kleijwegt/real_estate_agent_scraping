#!/usr/bin/env python3
'''
Script to load the data from a pickled database which is printed and exported to an excel so a user can view the content.
'''
import pandas
import os

HOUSE_DATA_FILE_NAME = "house_data_default.pkl"
directory = os.path.dirname(os.path.abspath(__file__))
HOUSE_DATA_PATH = os.path.join(directory, HOUSE_DATA_FILE_NAME)

def display_house_data(path):
    house_data = pandas.read_pickle(path)
    # house_data.style
    house_data.style.set_properties(**{'text-align': 'center'})

    print(house_data)
    print("Finished printing the saved house database.")


def export_data_frame_to_excel(path_data_frame, path_output_file):
    house_data = pandas.read_pickle(path_data_frame)
    house_data.to_excel(path_output_file, sheet_name="house_data")


if __name__ == "__main__":
    display_house_data(HOUSE_DATA_PATH)
    export_data_frame_to_excel(HOUSE_DATA_PATH, HOUSE_DATA_PATH.replace("pkl", "xlsx"))
