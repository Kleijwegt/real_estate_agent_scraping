#! /usr/bin/python3
# Script that is regularly called via a cron job to update the database of houses. It both updates the current database
# and saves it as a python pickle and exports the data to a local folder and shared google drive.
# The local folder is shared via a python server over the local network.
import time
import numpy
import os
from datetime import date
from update_real_estate_data import update_real_estate_data
from load_and_display_database import export_data_frame_to_excel, HOUSE_DATA_FILE_NAME

directory = os.path.dirname(os.path.abspath(__file__))
HOUSE_DATA_PATH = os.path.join(directory, HOUSE_DATA_FILE_NAME)

# To prevent the websites from noticing that a request is made regularly (with the cron job interval), I have added a
# random waiting time.
sleep_minutes = numpy.random.uniform(2, 20, 1)
sleep_seconds = numpy.random.uniform(1, 36, 1)
print("Introduced a random waiting time of %s minutes and %s seconds starting from %s." %
      (int(sleep_minutes), int(sleep_seconds), time.strftime("%H:%M:%S")))

time_to_wait = int(sleep_minutes * 60 + sleep_seconds)
while time_to_wait: 
    mins, secs = divmod(time_to_wait, 60) 
    timer = 'Time remaining before updating the real estate data base {:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r") 
    time.sleep(5)  # Update waiting time with a 10 second interval
    time_to_wait -= 5
    
timer = 'Time remaining before updating the real estate data base {:02d}:{:02d}'.format(mins, secs)

update_real_estate_data(HOUSE_DATA_PATH, new_database=False)

# Hardcoded path of the place to where the databases are exported (one folder shared via google drive and one via a python server)
export_data_frame_to_excel(HOUSE_DATA_PATH, "/home/Desktop/house_data/auto_update_of_" + date.today().strftime("%d-%m-%Y") + ".xlsx")
export_data_frame_to_excel(HOUSE_DATA_PATH, "/home/gdrive/house_data/auto_update_of_" + date.today().strftime("%d-%m-%Y") + ".xlsx")
