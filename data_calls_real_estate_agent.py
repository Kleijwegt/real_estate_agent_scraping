'''
Functions with calls to real estate agents that return the houses currently offered on their website.
Some return a filtered output, some don't. Check the docstring/return values to find this.
'''
import json
import re
import requests
from lxml import html

from requests_headers import get_random_header

MAX_PRICE = 750000
MIN_AREA = 60

def get_arnold_taal_data():
    """
    Gets and filters houses which fulfill to the set criteria (MAX_PRICE, MIN_AREA) from the real estate agent the function
    is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses, bool with if these houses are filtered (All true since the houses are filtered.)
    """
    url = "https://arnoldtaal.nl/aanbod/?type=koop&vraagprijs_min=&vraagprijs_max=400.000&huurprijs_min=&huurprijs_max=&aantal_kamers=&woonoppervlakte=100&orderby=date&order=DESC"
    # Make a GET request to fetch the raw HTML content
    url_page = requests.get(url, headers=get_random_header())
    url_tree = html.fromstring(url_page.content)

    i = 0
    arnold_adress_list = []
    arnold_url_list = []
    while True:
        try:
            i += 1
            adress = url_tree.xpath('/html/body/div[1]/div/div/div/div/div[1]/ul/li[' + str(i) + ']/a/h2')[0].text
            arnold_adress_list.append(adress)
            arnold_url_list.append("https://arnoldtaal.nl/" + adress.replace(" ", "-") + "/")
        except:
            break

    print("Content found")
    return arnold_adress_list, arnold_url_list, ([True] * len(arnold_adress_list))

def get_frisia_makelaars_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url_page = requests.get('https://frisiamakelaars.nl/api/properties/available.json?nocache=1606245139209', headers=get_random_header())
    url_tree = html.fromstring(url_page.content)
    frisia_house_data = json.loads(url_tree.text)['objects']

    def _frisia_match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        # for_sale
        if not data['object_registration'] == 'In verkoop genomen':
            return
        if not data['availability_status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['buy_price'] < price_max:
            return
        # right_city
        if not data['place'] == "'s-Gravenhage":
            return
        # big_enough
        if not min_area < data['usable_area_living_function']:
            return
        return data['street_name'] + " " + data["house_number"], data["url"]

    house_list = []
    url_list = []
    for house in frisia_house_data:
        if _frisia_match_check(house):
            house_list.append(_frisia_match_check(house)[0])
            url_list.append(_frisia_match_check(house)[1])

    print("Content found")
    return house_list, url_list

def get_bvl_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses, bool with if these houses are filtered (All false no fitlering in this function is applied)
    """
    # TODO Add filtering on area of the house
    # Burger van leeuwen huizen.
    url="https://bvl.nl/woningen/koop/s-gravenhage/#HctdCsMgEATgu-yzFFuaFy_RA5RSVl2oVbPiT9IScvcsmafhG2aDjJESYgXzBLuky5zgpSAyl88YomcFBaWGbwOzyeEnep-0BHYFK_P8KIXqkjB2ku2qdb7Jhaunav8ibrTO-X2CweZUGTYFhz2Qxz6y8dQc7Ac"
    # Make a GET request to fetch the raw HTML content
    url_page = requests.get(url, headers=get_random_header())
    url_tree = html.fromstring(url_page.content)

    bvl_adress_list = []
    link_list = []

    adress_list = [i.text for i in url_tree.xpath('//div[@class="card__inner"]')[0].xpath('//div[@itemprop="streetAddress"]/h3')]
    price_list = [i.text for i in url_tree.xpath('//div[@class="card__inner"]')[0].xpath('//div[@class="card__price prose fl clean fancy"]/p')]

    for adress, price in zip(adress_list, price_list):
        price = int(re.findall(r'\d+', price.replace(".", ""))[0])
        if price <= MAX_PRICE:
            bvl_adress_list.append(adress)
            link_list.append("https://bvl.nl/woningen/koop/s-gravenhage/"+adress.replace(" ", "-"))


    print("Content found")
    return bvl_adress_list, link_list, ([False] * len(bvl_adress_list))

def get_langezaal_data():
    """
    Gets and filters houses which fulfill to the set criteria (MAX_PRICE, MIN_AREA) from the real estate agent the function
    is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses, bool with if these houses are filtered (All true since the houses are filtered.)
    """
    url_page = requests.get('https://www.langezaal.nl/nl/realtime-listings/consumer', headers=get_random_header())
    url_tree = html.fromstring(url_page.content)
    house_data = json.loads(url_tree.text)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['address'], "https://www.langezaal.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list, ([True] * len(house_list))

def get_elzenaar_data():
    """
    Gets and filters houses which fulfill to the set criteria (MAX_PRICE, MIN_AREA) from the real estate agent the function
    is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses, bool with if these houses are filtered (All true since the houses are filtered.))
    """
    url_page = requests.get('https://www.elzenaar.com/nl/realtime-listings/consumer', headers=get_random_header())
    url_tree = html.fromstring(url_page.content)
    house_data = json.loads(url_tree.text)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['address'], "https://www.elzenaar.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list, ([True] * len(house_list))

def get_oltshoorn_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """

    url = "https://www.olsthoornmakelaars.nl/aanbod/"
    # Make a GET request to fetch the raw HTML content
    url_page = requests.get(url, headers=get_random_header())
    url_tree = html.fromstring(url_page.content)

    i = 0
    adress_list = []
    url_list = []
    while True:
        try:
            i += 1
            adress = url_tree.xpath('/html/body/div[2]/div[9]/div/div[2]/div[2]/div[1]/div[' + str(i) + ']/div[2]/div[2]/a[2]')[0].text
            adress_list.append(adress)
            url_list.append("https://www.olsthoornmakelaars.nl/aanbod/" + adress.replace(" ", "-") + "/")
        except:
            break

    print("Content found")
    return adress_list, url_list

def get_estata_data():
    """
    Gets and filters houses which fulfill to the set criteria (MAX_PRICE, MIN_AREA) from the real estate agent the function
    is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses, bool with if these houses are filtered (All true since the houses are filtered.)
    """
    url_page = requests.get('https://www.estata.nl/nl/realtime-listings/consumer', headers=get_random_header())
    house_data = json.loads(url_page.content)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['address'], "https://www.estata.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list, ([True] * len(house_list))

def get_nelisse_data():
    """
    Gets and filters houses which fulfill to the set criteria (MAX_PRICE, MIN_AREA) from the real estate agent the function
    is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses, bool with if these houses are filtered (All true since the houses are filtered.)
    """
    url_page = requests.get('https://www.nelisse.nl/nl/realtime-listings/consumer', headers=get_random_header())
    house_data = json.loads(url_page.content)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['address'], "https://www.nelisse.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list, ([True] * len(house_list))

def get_doen_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url_page = requests.get('https://www.doenmakelaars.com/nl/realtime-listings/consumer', headers=get_random_header())
    house_data = json.loads(url_page.content)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['address'], "https://www.doenmakelaars.com/" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list

def get_belderbos_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url_page = requests.get('https://www.belderbos.nl/nl/realtime-listings/consumer', headers=get_random_header())
    house_data = json.loads(url_page.content)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['url'], "https://www.belderbos.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list

def get_van_aalst_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url_page = requests.get('https://www.vanaalstmakelaars.nl/nl/realtime-listings/consumer', headers=get_random_header())
    house_data = json.loads(url_page.content)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['address'], "www.vanaalstmakelaars.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list

def get_hekking_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url_page = requests.get('https://www.hekking.nl/nl/realtime-listings/consumer', headers=get_random_header())
    house_data = json.loads(url_page.content)

    def _match_check(data, price_max=MAX_PRICE, min_area=MIN_AREA):
        if not data['isSales']:
            return
        if not data['status'] == 'Beschikbaar':
            return
        # right_price
        if not 1e5 < data['salesPrice'] < price_max:
            return
        # right_city
        if not data['city'] == "Den Haag":
            return
        # big_enough
        if not min_area < data['livingSurface']:
            return
        return data['url'], "www.hekking.nl" + data["url"]

    house_list = []
    url_list = []
    for house in house_data:
        if _match_check(house):
            house_list.append(_match_check(house)[0])
            url_list.append(_match_check(house)[1])

    print("Content found")
    return house_list, url_list

def get_klap_makelaars_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url = "https://www.klapmakelaardij.nl/aanbod/woningaanbod/'S-GRAVENHAGE/100+woonopp/-400000/koop/"
    # Make a GET request to fetch the raw HTML content
    url_page = requests.get(url, headers=get_random_header())
    url_tree = html.fromstring(url_page.content)

    klap_adress_list = []
    link_list = []

    adress_list = [i.text for i in url_tree.xpath('//h3[@class="street-address"]')]
    price_list = [i.text for i in url_tree.xpath('//span[@class="kenmerk first koopprijs"]/span[@class="kenmerkValue"]')]
    area_list = [i.text for i in
                  url_tree.xpath('//span[@class="kenmerk first woonoppervlakte"]/span[@class="kenmerkValue"]')]
    partially_link_list = list(set(i.get("href") for i in url_tree.xpath('//a[@class="aanbodEntryLink"]')))

    for adress, price, area, link in zip(adress_list, price_list, area_list, partially_link_list):
        price = int(re.findall(r'\d+', price.replace(".", ""))[0])
        area = int(re.findall(r'\d+', area)[0])
        if price <= MAX_PRICE:
            if area >= MIN_AREA:
                klap_adress_list.append(adress)
                link_list.append("https://www.klapmakelaardij.nl"+ link)


    print("Content found")
    return klap_adress_list, link_list

def get_diva_makelaars_data():
    """
    Gets houses from the real estate agent the function is named after.

    :return(tuple): List of addresses, list of url's of the filtered houses
    """
    url = "https://www.divamakelaars.nl/woningaanbod/koop/den-haag?locationofinterest=Den%20Haag&minlivablearea=100&moveunavailablelistingstothebottom=true&orderby=2&pricerange.maxprice=400000"
    # Make a GET request to fetch the raw HTML content
    url_page = requests.get(url, headers=get_random_header())
    url_tree = html.fromstring(url_page.content)

    full_adress_list = []
    full_link_list = []

    adress_list = [i.text for i in url_tree.xpath('//div[@class="obj_address_container"]/span')]
    partially_link_list = [i.get('href') for i in url_tree.xpath('//div[@class="datacontainer"]/a')]


    for adress, link in zip(adress_list, partially_link_list):
        full_adress_list.append(adress)
        full_link_list.append("https://www.divamakelaars.nl/" + link)


    print("Content found")
    return full_adress_list, full_link_list