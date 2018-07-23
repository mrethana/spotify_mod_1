from apidata_genreartist import *
#append any albums we need for comparison in url_album_ids
#function get list of API's to call for each artist's top tracks
def url_artist_top_tracks():
    x=[id for id in dict_of_ids.values()]
    return ["https://api.spotify.com/v1/artists/{id}/top-tracks".format(id=artist_id)+'?country=US' for artist_id in x]

#function to get list of dictionaries with each artist's top tracks (all coming from dict of artist id's)
def top_tracks_dict():
    list_dicts = []
    for url in url_artist_top_tracks():
        response_artists = requests.get(url, headers=headers)
        track_dict = json.loads(response_artists.content)
        list_dicts.extend(track_dict['tracks'])
    return list_dicts
top_tracks_dict = top_tracks_dict() #variable for dictionary of top tracks



#Get artist top tracks
all_track_ids = []
all_album_ids = []
def artist_top_tracks(top_tracks_dict):
    #local variable, artist-dependent
    top_track_ids = []
    for item in top_tracks_dict:
        top_track_ids.append(item['id'])
        all_track_ids.append(item['id'])
        #check to see if album isn't already in all_album_ids list before adding to the list:
        all_album_ids.append(item['album']['id'])
    return top_track_ids

def check_top_track(top_tracks, spotify_id):
    if spotify_id in top_tracks:
        return True
    else:
        return False


top_tracks = artist_top_tracks(top_tracks_dict) #list of top tracks

#dictionary of frequency of albums per artist- only return top 2
def album_freq_dict(all_album_ids):
    all_ids = [{'id' :album, 'freq':all_album_ids.count(album)} for album in set(all_album_ids)]
    return sorted(all_ids, key = lambda k :k['freq'], reverse = True)[:4]

#urls for get album API's for each album id
def url_album_ids():
    list_album_ids = [album['id'] for album in album_freq_dict(all_album_ids)]
    list_album_ids.append('0xi4cOWPUHjctyYU8ypCOB') #append marshmello album
    list_album_ids.append('3OZgEywV4krCZ814pTJWr7') #append ariana
    list_album_ids.append('2ANVost0y2y52ema1E9xAZ') #append mj
    merge = '%2c'.join(list_album_ids)
    return "https://api.spotify.com/v1/albums"+ "?ids=" + merge

#to call API for all albums
response_albums = requests.get(url_album_ids(), headers=headers)
albums_raw = json.loads(response_albums.content)
albums_clean = [album for album in albums_raw['albums']]
#dictionary with keys as Album name and values as list of tracks
album_tracks_dict = {album['name']:album['tracks'] for album in albums_clean}

all_albums = []
#create album objects

# def album_objects():
#    for album in albums_clean:
#        artist_obj = [artist for artist in all_artists if artist.spotify_id == album['artists'][0]['id']][0]
#        artist_id = artist_obj.id
#        all_albums.append(Album(spotify_id=album['id'], name=album['name'], release_date=album['release_date'], artist = artist_obj, artist_id = artist_id))
#    return all_albums
# album_objects()
#
# def add_albums():
#     for album in all_albums:
#         db.session.add(album)
#         db.session.commit()
# add_albums()

#function to get list of track_ids from all albums we pulled

def list_all_tracks():
    all_song_id_list = []
    for track in album_tracks_dict.values():
        song_ids_per_album = [item['id'] for item in track['items']]
        all_song_id_list.extend(song_ids_per_album)
    all_track_ids.extend(all_song_id_list)
    return list(set(all_track_ids))
