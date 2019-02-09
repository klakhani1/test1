#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests, json

def search_businesses(search_term, search_location):

    api_key = "_JnBPi2QeXRYaSqoYutrlVBoqVQp_UYELb6MUSRKWBWmPCFnesM9S1leyTV6FYqiqoGi3k_EPZXctlVWDH4cuEoriv_smBiwUk6A8-F8t38WT-59HSHYb5wVBNhVXHYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = json.loads(businesses_object.text)

    businesses_list = businesses_dict['businesses']

    print(businesses_dict)
    list_of_businesses = []
    for each in businesses_list:
        list_of_businesses.append(each)
    return list_of_businesses
