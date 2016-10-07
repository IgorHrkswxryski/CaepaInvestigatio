import glob
import json
import os
import mongoengine
import connect
from ORM import collect

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
                return
        send_db(myJSON)


def send_db(data):
    # insert JSON files into mongoDB
    try:
        collect.Collect(**data).save()
    except mongoengine.NotUniqueError:
        c = collect.Collect.objects(hiddenService=data['hiddenService']).first()
        c.update(**data)
    except:
        print('ERROR send to db')
