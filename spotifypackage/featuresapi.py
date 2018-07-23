from createtracks import *
# import pdb
#features for all songs API
feature_apis = []
def url_features(a,b):
    merge = '%2C'.join(list_all_tracks()[a:b])
    feature_apis.append("https://api.spotify.com/v1/audio-features" + "?ids=" + merge)
    return feature_apis
url_features(0,50)
url_features(50,100)
url_features(100,150)
url_features(150,200)
url_features(200,250)

def features_dict():
    features_dicts = []
    for url in feature_apis:
        response_features = requests.get(url, headers=headers)
        track_features = json.loads(response_features.content)
        features_dicts.extend(track_features['audio_features'])
    return features_dicts
all_features_dict = features_dict()


feature_list = ['danceability', 'energy','acousticness', 'valence', 'tempo']

all_features = []
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

def feature_values(track_id, feature_list, all_features_dict):
   feature_values_dict = {}
   for feat in feature_list:
       for item in all_features_dict:
           if item['id'] == track_id:
               feature_values_dict[feat] = item[feat]
   return feature_values_dict

track_features_list = []
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
