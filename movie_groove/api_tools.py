# Standard library
import json
from urllib import urlopen, quote_plus as urlencode

# OMDB Movie object
class Movie(object):
    def __init__(self, json):
        self.title = json['Title']
        self.year = json['Year']
        self.plot = json['Plot']
        self.runtime = json['Runtime']
        self.rating = json['imdbRating']
        self.votes = json['imdbVotes']
        self.director = json['Director']
        self.writer = json['Writer']
        self.actors = json['Actors']
        self.url = "http://www.imdb.com/title/" + json['imdbID'] + "/"

# Spotify Track object
class Track(object):
    def __init__(self, json):
        self.album_name = json['album']['name']
        self.album_year = json['album']['released']
        self.name = json['name']
        self.href = json['href']
        self.artists = [artist['name'] for artist in json['artists']]
        self.artist = self.artists[0]


# Returns a movie based on the query
def get_movie(query):
    movie = None
    # HTTP request to IMDB API
    r = urlopen('http://omdbapi.com/?t=' + urlencode(query))
    # Decode from JSON
    movie_data = json.load(r)
    # Check if the response was successful
    if movie_data['Response'] != 'False':
        # Create our Movie object
        movie = Movie(movie_data)
    return movie

# Return tracks based on the query
def get_tracks(query):
    tracks = []
    # HTTP request to Spotify API
    r = urlopen('http://ws.spotify.com/search/1/track.json?q=' + urlencode(query))
    # Decode from JSON
    tracks_data = json.load(r)
    # Check that we recieved some tracks
    if len(tracks_data['tracks']) > 0:
        # Get the first 5 tracks
        for track in tracks_data['tracks'][:5]:
            # Append a Track object to the list of tracks
            tracks.append(Track(track))

    return tracks

