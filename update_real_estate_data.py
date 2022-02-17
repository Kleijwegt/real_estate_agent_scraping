#!/usr/bin/env python3
'''
Script to update all the data of a real estate agent database with new data.
Can be run as a script directly or via the use of the function 'update_real_estate_data'
'''
import os
import numpy
import pandas

from load_and_display_database import export_data_frame_to_excel, HOUSE_DATA_FILE_NAME
from data_calls_real_estate_agent import get_arnold_taal_data,\
                        get_bvl_data, get_langezaal_data, get_elzenaar_data, get_oltshoorn_data, get_estata_data, \
                        get_nelisse_data, get_doen_data, get_van_aalst_data, \
                        get_belderbos_data, get_hekking_data, get_klap_makelaars_data, get_diva_makelaars_data,\
                        get_frisia_makelaars_data, get_oltshoorn_data\

# Only functions which reliably provided data are added to this list.
real_estate_agent_functions = [get_arnold_taal_data, get_oltshoorn_data, get_frisia_makelaars_data,
                               get_bvl_data, get_langezaal_data,
                               get_elzenaar_data, get_oltshoorn_data, get_estata_data, get_nelisse_data, get_doen_data,
                               get_belderbos_data, get_van_aalst_data, get_hekking_data, get_klap_makelaars_data,
                               get_diva_makelaars_data]

directory = os.path.dirname(os.path.abspath(__file__))
HOUSE_DATA_PATH = os.path.join(directory, HOUSE_DATA_FILE_NAME)

COLUMNS_DATA = ("Address", "Link", "Name real estate agent", "specs checked", "first found", "last found", "available")

def update_real_estate_data(path, new_database=False):
    new_house_data = get_current_data_of_all_real_estate_agents()
    # Get column name from the end so that extra columns can be added in the middle if needed.
    new_house_data[COLUMNS_DATA[-3]] = numpy.nan
    new_house_data[COLUMNS_DATA[-2]] = pandas.Timestamp.now()
    new_house_data[COLUMNS_DATA[-1]] = True

    if not new_database:
        old_house_data = pandas.read_pickle(path)
        # Set all old house to non available, if still availbe this value is overwritten
        old_house_data[COLUMNS_DATA[-1]] = False
        house_market_data = new_house_data.combine_first(old_house_data)
    else:
        house_market_data = new_house_data
    # If the house hasn't been found before the first found data equals the last found date
    house_market_data = house_market_data.fillna(new_house_data["last found"][0])

    house_market_data.to_pickle(path)

    return house_market_data


def get_current_data_of_all_real_estate_agents():
    house_data = pandas.DataFrame(columns=COLUMNS_DATA)

    # Get new data
    for real_estate_agent in real_estate_agent_functions:
        try:
            data_real_estate_agent = real_estate_agent()
            adresses = data_real_estate_agent[0]
            links = data_real_estate_agent[1]
            specs_checked = (data_real_estate_agent[2] if len(data_real_estate_agent) >= 3 else ["?"] * len(adresses))
            # Derive the name of the real estate agent via the name of the function.
            name_real_estate_agent = real_estate_agent.__name__[real_estate_agent.__name__.find("_") + 1:
                                              real_estate_agent.__name__.rfind("_")].replace("_", " ")

            data_frame_real_estate_agent = pandas.DataFrame({COLUMNS_DATA[0]: adresses,
                                                    COLUMNS_DATA[1]: links,
                                                    COLUMNS_DATA[2]: name_real_estate_agent,
                                                    COLUMNS_DATA[3]: specs_checked}, columns=COLUMNS_DATA)
            house_data = house_data.append(data_frame_real_estate_agent, ignore_index=True)
        except Exception:
            name_real_estate_agent = real_estate_agent.__name__[real_estate_agent.__name__.find("_") + 1:
                                              real_estate_agent.__name__.rfind("_")].replace("_", " ")
            print("Failed to get data for %s" % name_real_estate_agent)

    return house_data


if __name__ == "__main__":
    update_real_estate_data(HOUSE_DATA_PATH, new_database=True)
    export_data_frame_to_excel(HOUSE_DATA_PATH, HOUSE_DATA_PATH.replace("pkl", "xlsx"))


