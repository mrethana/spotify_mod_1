from config import *
from models import *
import pdb

#to add: check artist genre using artist_clean and add them to that respective list in config
#this will update the genre_artist

#function to format all artist id's properly for API
def url_of_artist_ids():
    x=[id for id in dict_of_ids.values()]
    merge = '%2C'.join(x)
    return "https://api.spotify.com/v1/artists" + "?ids=" + merge


#to call API for all artists
response_artists = requests.get(url_of_artist_ids(), headers=headers)
artists_raw = json.loads(response_artists.content)
artists_clean = [artist for artist in artists_raw['artists']]


#call all genres api
def get_all_genres():
    url_genres_all = 'https://api.spotify.com/v1/browse/categories?country=US'
    response_genres = requests.get(url_genres_all, headers=headers)
    genres_raw = json.loads(response_genres.content)
    return [Genre(name = genre['id']) for genre in genres_raw['categories']['items']]
genre_obj_list = get_all_genres()

#Create genres for artists

def genre_artist(spotify_id):
    if spotify_id == "64KEffDW9EtZ1y2vBYgq8T":
        genre = 'edm_dance'
    elif spotify_id in pop_list:
        genre = 'pop'
    elif spotify_id in hiphop_list:
        genre = 'hiphop'
    return genre


def find_or_create_genre(genre_name):
   for item in genre_obj_list:
       if genre_name == item.name:
           return item

#creating several Artists objects pass through artists_clean
all_artists = []
# def artist(data):
#     for item in data:
#         name = item['name']
#         spotify_id = item['id']
#         popularity = item['popularity']
#         followers = item['followers']['total']
#         genre_name = genre_artist(spotify_id)
#         genre = find_or_create_genre(genre_name)
#         all_artists.append(Artist(spotify_id=spotify_id, name=name, artist_popularity=popularity, followers=followers, genre = genre))
#     return all_artists
#
# artist(artists_clean)
#
# def add_artist_objects():
#     for artist in all_artists:
#         db.session.add(artist)
#         db.session.commit()
# add_artist_objects()
# def add_genre_objects():
#     for genre in genre_obj_list:
#         db.session.add(genre)
#         db.session.commit()
#
# add_genre_objects()
