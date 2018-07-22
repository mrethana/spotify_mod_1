import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}

#Key for api's
api_key = "BQD-3Vm2vfOLVVwsoTY0gBlUecfh0pjOceO13M0HMbSQs3R0gNfqKI6fJQbaGT4GoQgA7prYWp7N6PJkOuFz3HIvHLJuDR0J_5elCpps53qQObEEmPWDJq5piqYY7cKuzp0LKMcjBkMO"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
