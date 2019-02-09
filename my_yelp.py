
   businesses_dict = json.loads(businesses_object.text)







    businesses_list = businesses_dict['businesses']



    #







    print(businesses_dict)



    list_of_businesses = []



    for each in businesses_list:



        list_of_businesses.append(each)



    return list_of_businesses
