import pandas as pd
from facepy import GraphAPI
import json
import requests

access_token="EAAXkpg46iwUBACry9LZCZC0KLZAuhil9c0XXExTR2YRe7LSDlLtbuMZAZBDSRuowP6bp5SEcIKjyMwLUOZBhBvDAb7adSzRAubaFjVLJjZBdZAuLbbDJFDE7uwsYMwodRfsHczTvLWdLSo6v9ZALISPzclhKjFnZA6Dm8bCwM2rHJyzSFS5u83JJg48lm7VTQpwSqEZAkzIB3ZCOxBJ2IwJauPQf9LzZCp6lJNVXQQNnq9Hwul34qsSzwl3y3"

app_id ="1658776737975045"

graph=GraphAPI(access_token)

groupIDs =("[429634238102495]")


for gID in groupIDs:
    groupData = graph.get(gID + "/feed", page=True, retry=3, limit=500)
    print(groupData)


    # for data in groupData:
    #         json_data=json.dumps(data, indent = 4,cls=DecimalEncoder)
    #         decoded_response = json_data.decode("UTF-8")
    #         data = json.loads(decoded_response)
    #         print "Paging group data..."
    #
    #         for item in data["data"]:
    #             ...etc, dealing with items...


from pyfacebook import GraphAPI

from pyfacebook import GraphAPI
api=GraphAPI(access_token=access_token)


