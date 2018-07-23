import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG",'mj':"3fMbdgg4jU18AjLCKBhRSm", 'biggie':"5me0Irg2ANcsgc93uaYrpb",'crow':"4TKTii6gnOnUXQHyuo9JaD",'aerosmith':'7Ey4PD4MYsKc5I2dolUwbH','carrie' : '4xFUf1FHVy696Q1JQZMTRj', 'gees' : '1LZEQNv7sE11VDY3SdxQeN', 'fall_out' : '4UXqAaa6dQYAk18Lv7PEgX'}

pop_list = ["6VuMaDnrHyPL1p4EHjYLi7","3fMbdgg4jU18AjLCKBhRSm"]
hiphop_list = ["6oMuImdp5ZcFhWP0ESe6mG","5me0Irg2ANcsgc93uaYrpb"]
rock_list = ['7Ey4PD4MYsKc5I2dolUwbH','4UXqAaa6dQYAk18Lv7PEgX']
country_list = ["4TKTii6gnOnUXQHyuo9JaD",'4xFUf1FHVy696Q1JQZMTRj']
edm_dance_list = ["64KEffDW9EtZ1y2vBYgq8T", "1LZEQNv7sE11VDY3SdxQeN"]

#Key for api's
api_key = "BQD2iC2L71M026KDkA6G7m2agdTbh-00888bTtN4xiUpFxTygZN7UnZPlRJbm_PFkPsXPc6xhNPWLG2lyAQf4gkSlPzpBm_iBeLfb8DES4Wch2GY4dUpmI_qX5O35efVrSgiXMXyALFA"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
