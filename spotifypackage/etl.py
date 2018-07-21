from spotifypackage.featuresapi import *
# import pdb
#converts artist object to artist name
for artist in Artist.query.all():
    if artist.name == 'Migos':
        migos = artist
    elif artist.name == 'Marshmello':
        marshmello = artist
    elif artist.name == 'Charlie Puth':
        puth = artist

def artist_name_by_obj(artist_object):
    for artist in Artist.query.all():
        if artist_object == artist:
            name = artist.name
            return name
#return list of tuples for all artist, track pairs
def all_track_names_artist():
    return [(track.name, artist_name_by_obj(track.artist)) for track in  Track.query.all()]

def track_obj_by_name(name):
    return [track for track in Track.query.all() if track.name == name][0]

def feature_name_by_id(id):
    return [feature.name for feature in Feature.query.all() if feature.id == id][0]

def artist_obj_by_track_id(id):
    return [track.artist for track in Track.query.all() if track.id == id][0]

def pull_track_features_by_track(name):
    obj = track_obj_by_name(name)
    obj_id = obj.id
    # for trackfeature in TrackFeature.query.all():
    #     id = trackfeature.track_id
    #     value = trackfeature.value
    #     pdb.set_trace()
    return [(feature_name_by_id(trackfeature.feature_id) ,trackfeature.value) for trackfeature in TrackFeature.query.all() if trackfeature.track_id == obj_id]

def tracks_for_artist(artist_name):
    tracks = []
    for pair in all_track_names_artist():
        if pair[1] == artist_name:
            tracks.append(pair[0])
    return tracks

def all_featurevalue_artist(artist):
    feature_values = []
    artist_tracks = tracks_for_artist(artist)
    for track in artist_tracks:
        feature_values.append({track:pull_track_features_by_track(track)})
    return feature_values

# def avg_feature_values(feature_name, artist_name):
#     x = [tf.value for tf in TrackFeature.query.all() if feature_name == feature_name_by_id(tf.feature_id) and artist_name == artist_name_by_obj(artist_obj_by_track_id(tf.track_id))]
#     return round(sum(x)/len(x),2)
#
# def avg_featurevalues_artist(artist):
#     feature_names = [feature.name for feature in Feature.query.all()]
#     return {feature:avg_feature_values(feature,artist) for feature in feature_names}

def feature_values_average(feature, artist):
   dict_values = [value for value in all_featurevalue_artist(artist)]
   feature_values_list = [tup[1] for item in dict_values for value in item.values() for tup in value if tup[0] == feature]
   return round(sum(feature_values_list)/len(feature_values_list),2)

def feature_names():
   return [feature.name for feature in Feature.query.all()]

def avg_featurevalues_artist(artist, feature_names_list):
   return {feature: feature_values_average(feature, artist) for feature in feature_names_list}



 # def avg_featurevalues_artist(genre, feature_names_list):
 #    return {feature: feature_values_average(feature, artist) for feature in feature_names_list}
