from spotifypackage import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(100))
    name = db.Column(db.String(100))
    artist_popularity = db.Column(db.Integer)
    followers  = db.Column(db.Integer)
    tracks = db.relationship('Track', back_populates = 'artist')
    albums = db.relationship('Album', back_populates = 'artist')
    genre = db.relationship('Genre',back_populates = 'artists')
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    spotify_id = db.Column(db.String(100))
    track_popularity = db.Column(db.Integer)
    featured_artist = db.Column(db.Boolean)
    top_track = db.Column(db.Boolean)
    features = db.relationship('Feature',secondary = 'track_features', back_populates = 'tracks')
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates = 'tracks')
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    album = db.relationship('Album', back_populates = 'tracks')
    playlists = db.relationship('Playlist', secondary = 'playlist_tracks', back_populates = 'tracks')
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genre = db.relationship('Genre', back_populates = 'tracks')


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key = True)
    spotify_id = db.Column(db.String(100))
    name = db.Column(db.String(100))
    release_date = db.Column(db.String(100))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates = 'albums')
    tracks = db.relationship('Track', back_populates = 'album')



class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key = True)
    spotify_id = db.Column(db.String(100))
    name = db.Column(db.String(100))
    tracks = db.relationship('Track', secondary = 'playlist_tracks', back_populates = 'playlists')
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genre = db.relationship('Genre', back_populates = 'playlists')

#
#
class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    playlists = db.relationship('Playlist', back_populates = 'genre')
    artists = db.relationship('Artist', back_populates = 'genre')
    tracks = db.relationship('Track', back_populates = 'genre')


class Feature(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    tracks = db.relationship('Track', secondary = 'track_features', back_populates = 'features')


# class ArtistGenre(db.Model):
#     __tablename__ = 'artist_genres'
#     id = db.Column(db.Integer, primary_key = True)
#     artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
#     genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
# #
# class TrackGenre(db.Model):
#     __tablename__ = 'track_genres'
#     id = db.Column(db.Integer, primary_key = True)
#     track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
#     genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

# class PlaylistTracks(db.Model):
#     __tablename__ = 'playlist_tracks'
#     id = db.Column(db.Integer, primary_key = True)
#     playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
#     track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
#
class TrackFeature(db.Model):
    __tablename__ = 'track_features'
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    feature_id = db.Column(db.Integer, db.ForeignKey('features.id'))
    track = db.relationship(Track, backref=db.backref('track_features', cascade='all, delete-orphan'))
    feature = db.relationship(Feature, backref=db.backref('track_features', cascade='all, delete-orphan'))


db.create_all()
