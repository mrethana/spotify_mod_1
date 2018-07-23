from spotifypackage.models import *
# from spotifypackage.dashboard import *
import pandas as pd
import pdb

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
def all_track_names_artist(top_track=False):
   if top_track==True:
       return [(track.name, artist_name_by_obj(track.artist)) for track in  Track.query.all()
       if track.top_track==True]
   else:
       return [(track.name, artist_name_by_obj(track.artist)) for track in  Track.query.all()
       if track.top_track==False]


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

def tracks_for_artist(artist_name, top_track=False):
   tracks = []
   for pair in all_track_names_artist(top_track):
       if pair[1] == artist_name:
           tracks.append(pair[0])
   return tracks

def all_featurevalue_artist(artist, top_track=False):
   feature_values = []
   artist_tracks = tracks_for_artist(artist, top_track)
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

def track_popularity():
   return {track.name: track.track_popularity for track in Track.query.all()}


def create_trace(artist, feature, title, marker, top_track=False):
   dict_values = [value for value in all_featurevalue_artist(artist, top_track)]
   popularity_dict = track_popularity()
   feature_dict = [{'name': key, feature:tuple[1], 'popularity': popularity_dict[key]} for item in dict_values for key,value in item.items() for tuple in value if tuple[0] == feature]
   x = [dict[feature] for dict in feature_dict]
   y = [dict['popularity'] for dict in feature_dict]
   text = [dict['name'] for dict in feature_dict]
   return dict(x=x, y=y, name=title, mode = 'markers', marker=marker,opacity = 0.7, text=text)

def marker_color(feature):
   if feature == 'danceability':
       color = 'red'
   elif feature == 'energy':
       color = 'blue'
   elif feature == 'acousticness':
       color = 'green'
   elif feature == 'valence':
       color = 'purple'
   elif feature == 'tempo':
       color = 'orange'
   return color

marker1 = dict(
size = 16,
color = 'green',)
marker2 = dict(
size = 16,
color = 'blue',
line = dict(
width = 2,))

def top_track_title(feature):
   return 'Top Tracks by ' + feature

def oth_track_title(feature):
   return 'Other Tracks by ' + feature


def list_of_traces(artist):
   top_track_trace_list = []
   oth_track_trace_list = []
   feature_names = [feature.name for feature in Feature.query.all()]
   for feature in feature_names:
       color = marker_color(feature)
       marker = dict(size = 12, color = color,line = dict(width = 2,))
       top_track_name = top_track_title(feature)
       oth_track_name = oth_track_title(feature)
       top_track_trace_list.append(create_trace(artist, feature, top_track_name , marker, top_track=True))
       oth_track_trace_list.append(create_trace(artist, feature, oth_track_name, marker))
   final_trace_list = [top_track_trace_list, oth_track_trace_list]
   return final_trace_list

def list_of_artists_for_dropdown():
   options = [{'label': 'All Artists', 'value': 'all_artists'}]
   artist_list = [artist.name for artist in Artist.query.all()]
   for artist in artist_list:
       options.append({'label': artist, 'value': artist})
   return options
def tempo_normalization(val):
   tempo_id = [feature.id for feature in Feature.query.all() if feature.name == 'tempo'][0]
   tempo_values = [tf.value for tf in TrackFeature.query.all() if tf.feature_id == tempo_id]
   min_val = min(tempo_values)
   max_val = max(tempo_values)
   # return [round(((val-min_val)/(max_val-min_val)),2) for val in tempo_values]
   tempo_val = round(((val-min_val)/(max_val-min_val)),2)
   return tempo_val

def tempo_normalization_list(tracks_list):
   for dict in tracks_list:
       if 'tempo' in dict['name']:
           for val in dict['x']:
               dict['x'][dict['x'].index(val)] = tempo_normalization(val)
   return tracks_list

def bar_trace(artist_name):
    avg_features = avg_featurevalues_artist(artist_name, feature_names())
    x = [feature for feature in avg_features.keys()]
    y = [value for value in avg_features.values()]
    y[4] = tempo_normalization(y[4])
    return {'x': x, 'y': y, 'type': 'bar', 'name': artist_name}

    #[{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Average Feature Values'}]

def all_bars():
    all_bars_list = []
    x = [artist.name for artist in Artist.query.all()]
    for artist in x:
        all_bars_list.append(bar_trace(artist))
    return all_bars_list

# def drake():
#     trace_list = list_of_traces('Drake')
#     top_tracks = tempo_normalization_list(trace_list[0])
#     oth_tracks = tempo_normalization_list(trace_list[1])
#     data = top_tracks + oth_tracks
#     return data
#dict(x=x, y=y, name=title, mode = 'markers', marker=marker, text=text)
 # def avg_featurevalues_artist(genre, feature_names_list):
 #    return {feature: feature_values_average(feature, artist) for feature in feature_names_list}
