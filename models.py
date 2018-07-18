
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(Integer, primary_key = True, autoincrement = False)
    name = db.Column(db.String(100))
    artist_popularity = db.Column(db.Integer)
    tracks = db.relationship('Track', back_populates = 'artist')
    albums = db.relationship('Album', back_populates = 'artist')
    genres = db.relationship('Genres',secondary = 'artist_genres' back_populates = 'artist')


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(Integer, primary_key = True,autoincrement = False)
    name = db.Column(db.String(100))
    track_popularity = db.Column(db.Integers)
    release_date = db.Column(db.Date)
    features = db.relationship('Feature',secondary = 'track_features', back_populates = 'tracks')
    artist_id = Column(db.Integers, ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates = 'tracks')
    album_id = db.Column(db.Integers, ForeignKey('albums.id'))
    album = db.relationship('Album', back_populates = 'tracks')
    playlists = db.relationship('Playlist', secondary = 'playlist_tracks', back_populates = 'tracks')
    genres = db.relationship('Genre', secondary = 'track_genres', back_populates = 'tracks')


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integers, primary_key = True, autoincrement = False)
    name = db.Column(db.String(100))
    artist_id = db.Column(db.Integers, ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates = 'albums')
    tracks = db.relationship('Track', back_populates = 'album')



class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key = True, autoincrement = False)
    name = db.Column(db.String(100))
    tracks = db.relationship('Track', secondary = 'playlist_tracks', back_populates = 'tracks')
    genre_id = db.Column(db.Integer, ForeignKey('genres.id'))
    genre = db.relationship('Genre', back_populates = 'playlists')



class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key = True, autoincrement = False)
    name = db.Column(db.String(100))
    playlists = db.relationship('Playlist', back_populates = 'genre')
    artists = db.relationship('Artist', secondary = 'artist_genres', back_populates = 'genres')
    tracks = db.relationship('Track', secondary = 'track_genres', back_populates = 'genres')

class Features(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    value = db.Column(db.Integer)
    tracks = db.relationship('Track', secondary = 'track_features', back_populates = 'features')


class ArtistGenre(db.Model):
    __tablename__ = 'artist_genres'
    id = db.Column(db.Integer, primary_key = True)
    artist_id = db.Column(db.Integer, ForeignKey('artists.id'))
    genre_id = db.Column(db.Integer, ForeignKey('genres.id'))

class TrackGenre(db.Model):
    __tablename__ = 'track_genres'
    id = db.Column(db.Integer, primary_key = True)
    track_id = db.Column(db.Integer, ForeignKey('tracks.id'))
    genre_id = db.Column(db.Integer, ForeignKey('genres.id'))

class PlaylistTracks(db.Model):
    __tablename__ = 'playlist_tracks'
    id = db.Column(db.Integer, primary_key = True)
    playlist_id = db.Column(db.Integer, ForeignKey('playlists.id'))
    track_id = db.Column(db.Integer, ForeignKey('tracks.id'))

class TrackFeatures(db.Model):
    __tablename__ = 'track_features'
    id = db.Column(db.Integer, primary_key = True)
    track_id = db.Column(db.Integer, ForeignKey('tracks.id'))
    feature_id = db.Column(db.Integer, ForeignKey('features.id'))
