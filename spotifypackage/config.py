import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}

#Key for api's
api_key = "BQAWe23WX2IubRWa8KFrxF0wk4fGlWGdvc_M2_f5ET80plPsb3KUQchl1wEjoaKbDi1hA_APGeMwsSOnahNpP4oCkAIszmnTpUHdYqN37Am9qdFnt_dPXRawChv927MHD0S6B7WzKRm3"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
