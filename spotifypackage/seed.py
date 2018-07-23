# from featuresapi import *
#
#
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
#
# def add_genre_objects():
#     for genre in genre_obj_list:
#         db.session.add(genre)
#         db.session.commit()
#
# add_genre_objects()
#
#
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
#
# def track_objects(final_all_tracks, track_artist, all_artists):
#    for track in final_all_tracks:
#        spotify_id = track['id']
#        name = track['name']
#        track_popularity = track['popularity']
#        featured_artist = check_featured_artist(songs_with_feat_artist, spotify_id)
#        top_track = check_top_track(top_tracks, spotify_id)
#        artist = check_artist(spotify_id,track_artist, all_artists)
#        artist_id = return_artist_id(artist)
#        genre = return_artist_genre(artist)
#        genre_id = return_genre_id(genre)
#        all_track_objs.append(Track(spotify_id=spotify_id, name=name, track_popularity=track_popularity, featured_artist=featured_artist, top_track=top_track, artist=artist, artist_id=artist_id, genre=genre, genre_id=genre_id))
#    return all_track_objs
#
# track_objects(final_all_tracks, track_artist, all_artists)
#
# def add_track_objs():
#     for object in all_track_objs:
#         db.session.add(object)
#         db.session.commit()
# add_track_objs()
#
# def feature_objs(feature_list):
#     for feature in feature_list:
#         all_features.append(Feature(name=feature))
#     return all_features
# feature_objs(feature_list)
#
# def add_features():
#     for feature in all_features:
#         db.session.add(feature)
#         db.session.commit()
# add_features()
#
# def track_features_obj(all_features, all_features_dict, all_track_objs, feature_list):
#     for track in all_track_objs:
#         for feature in all_features:
#             track_id = track.spotify_id
#             feature_id = feature.id
#             feature_value = feature_values(track_id, feature_list, all_features_dict)
#             value = feature_value[feature.name]
#             track_feature = TrackFeature(track_id=track_id, feature_id=feature_id, value=value)
#             feature.track_features.append(track_feature)
#             # print(feature.track_features)
#             track.track_features.append(track_feature)
#             # print(track.track_features)
#             track_features_list.append(track_feature)
#             # pdb.set_trace()
#     return track_features_list
#
#
# track_features_obj(all_features, all_features_dict, all_track_objs, feature_list)
#
# def add_track_features():
#     for feature in track_features_list:
#         db.session.add(feature)
#         db.session.commit()
# add_track_features()
