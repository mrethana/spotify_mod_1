import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG",'mj':"3fMbdgg4jU18AjLCKBhRSm", 'biggie':"5me0Irg2ANcsgc93uaYrpb",'crow':"4TKTii6gnOnUXQHyuo9JaD",'aerosmith':'7Ey4PD4MYsKc5I2dolUwbH'}

pop_list = ["6VuMaDnrHyPL1p4EHjYLi7","3fMbdgg4jU18AjLCKBhRSm"]
hiphop_list = ["6oMuImdp5ZcFhWP0ESe6mG","5me0Irg2ANcsgc93uaYrpb"]
rock_list = ['7Ey4PD4MYsKc5I2dolUwbH']
country_list = ["4TKTii6gnOnUXQHyuo9JaD"]

#Key for api's
api_key = "BQCbEXWGowHNumssyTKkQ3qw87SnHrSnCSihhJuMAevm260LZrl4iVIe24u-Oys9k8AavoaqoQ0YSOKBi540Drod0nzqspJafEQ1eAxbcvickmT5enCxsc6B1j75iWMuaCkugjD6-Fuw"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
