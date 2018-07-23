import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG",'mj':"3fMbdgg4jU18AjLCKBhRSm", 'drake':"3TVXtAsR1Inumwj472S9r4",'camila':"4nDoRrQiYLoBzwC5BhVJzF",'ariana':'66CXWjxzNUsdJxJ2JdwvnR'}

pop_list = ["6VuMaDnrHyPL1p4EHjYLi7","3fMbdgg4jU18AjLCKBhRSm","4nDoRrQiYLoBzwC5BhVJzF",'66CXWjxzNUsdJxJ2JdwvnR']
hiphop_list = ["6oMuImdp5ZcFhWP0ESe6mG","3TVXtAsR1Inumwj472S9r4"]
#Key for api's
api_key = "BQBUrlssIKABgxu66JEXi-y-JhyiQRG0XNi9-XnsCF6iUwlivw5NlR1YfcpjbK9rDrGXdPKXABZlrVbvVkTgMvYGaGMuDh0KHXKD5T_48tkxapRkPzTBtsB03z8jB_dQK-atiRc11itt"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
