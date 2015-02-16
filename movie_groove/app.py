# coding: utf-8

# Flask
from flask import Flask, render_template, request
# Own stuff
from api_tools import get_movie, get_tracks


app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Search results
@app.route('/search')
def search():
    query = request.args.get('q')

    movie = None
    tracks = []

    # If there was a query in the GET request, fetch the movie and tracks
    if query:
        movie = get_movie(query)
        tracks = get_tracks(movie.title)

    # Render the search.html template with the movie and tracks
    return render_template('search.html', query=query, movie=movie, tracks=tracks)


if __name__ == '__main__':
    app.debug = True
    app.run()
