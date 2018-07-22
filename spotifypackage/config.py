import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}

#Key for api's
api_key = "BQAsT4uq4amYNoBGhorr3AHrLlrHGb13n9F5GmBa4fjy3KPPSsZHXQboaYXwrxV6mfn3zBcRQ47iK1kfzMBJTWVdzJtI2Weo0kwGtyFIlly4cWn7NTM66PRaI3q7lTQIzRhkHCRguErk"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
