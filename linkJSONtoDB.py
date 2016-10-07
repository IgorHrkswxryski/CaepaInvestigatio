import glob
import json
import os
import mongoengine
import connect
import collect

# env var to access .json files
files_list = glob.glob(os.environ['JSON_RESULTS']+"/*.json")

def JSONtoDB():
    """ browse and insert into mongoDB all json files """

    for json_file in files_list:
        with open(json_file) as data_file:

            # browse JSON files
            try:
                myJSON = json.load(data_file)
                print(myJSON['hiddenService'])
            except:
                print(json_file+".ERREUR")

            # insert JSON files into mongoDB
            try:
                collect.Collect(**myJSON).save()
            except mongoengine.NotUniqueError:
                c = collect.Collect.objects(hiddenService=myJSON['hiddenService']).first()
                c.update(**myJSON)
                #c.save()
            except:
                print('ERROR')
            #print("ERROR INSERTING"+json_file)

# coection to database
connect.connectionToDB()

#browse and insert into mongoDB all json files
JSONtoDB()
