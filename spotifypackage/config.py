import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}

#Key for api's
api_key = "BQBy1cESW3Pi2DW2mhPRfSjjGGOcXwjDAeVmFfbsgfdhWt4AS4Z3hlcf_NSNK6vcvYvuBNbR8iJ4KZrLGJGRXOVswKy05uUvbax3-ZTTk2zBb07Kk5nh2ikCCg8wbns0UWqBIQNasQe5"
#Headers for Spotify API

headers = {'Accept': 'application/json',

'Content-Type': 'application/json',

'Authorization': 'Bearer {}'.format(api_key)}
