import pandas as pd
import json
import collections


##################################################################
#JSON memory storage - search, add, and delete
##################################################################
def main ():

    #d = {"location":{"state":"WA"},"active":True}
    #print (d.values())

    file = '/Users/prithvi/Downloads/test_cases_a3qmjka3jjm/input001.txt'
    data_list = []
    datastore = {}


    #Reading through the given file, line by line
    for line in open(file, 'r'):


        if line.__contains__("add"):
            new_add = line.replace("add", "").strip()   #gets rid of the "add" command and white spaces
            #data_list.append(new_add)   #adds only the JSON object to a list
            #print (data_list)

            datastore.update(json.loads(new_add))
            print (datastore)



        if line.__contains__("get"):
            #print (line)
            get_query = line.replace("get", "").strip()   #creates a query string
            #print (get_query)
            dict_query = json.loads(get_query)    #convert query string into json form, so a dictionary
            #compare_list = (dict_query.values())
            #print (compare_str)

            for i in range(len(data_list)):

                if get_query in data_list[i]:
                    print ("match")


            #flatten the two dictionaries for easy comparison
            #flat_df = flatten (dict_compare)
            #print (flat_df)
            #master_dict = remove_dups(flat_df)   #removed duplicates from the main dictionary
            #print (master_dict)
            flat_query = flatten (dict_query)
            #print (flat_query)

            flag = False

            for key in flat_query:
                #print (flat_query[key])
                pass

                #if flat_query[key] == flat_df[key]:
                    #pass


                #for key in flat_df:
                    #if flat_query[key] <= flat_df[key]:
                        #print ("match")




        print("#########")


        if line.__contains__("delete"):
            #print (line)
            remove = line.replace("delete", "").strip()     #creates a string to match for deletion

            #for row in data_df.iterrows():

                #if





    #print ("#####")
    #print (type(data_df["active"][0]))
    #print (data_df)




#################################
#Helper functions:
#################################

def flatten (d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def remove_dups (dct):
    reversed_dct = {}
    for key, val in dct.items():
        new_key = tuple(val["dst"]) + tuple(val["src"]) + (tuple(val["alias"]) if "alias" in val else (None,) )
        reversed_dct[new_key] = key
    result_dct = {}
    for key, val in reversed_dct.items():
        result_dct[val] = dct[val]
    return result_dct


#################################
if __name__== "__main__":
    main()

