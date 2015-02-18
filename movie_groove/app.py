# coding: utf-8

# Flask
from flask import Flask, render_template, request, jsonify
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

# API documentation
@app.route('/api/docs')
def documentation():
    return render_template('docs_v1.html')


# Our own API!
@app.route('/api/v1/search')
def search_api():
    # Title to search for
    query = request.args.get('q')
    # Set default values if parameters are not defined
    max_tracks = request.args.get('max_tracks') or 5
    
    # No movie title was provided
    if not query:
        # Return an error and set an appropriate status code
        return jsonify({'error': 'Bad Request',
                        'code': 400,
                        'message': 'No movie title was provided'
                        }), 400
    # Try converting parameter to integers
    try:
        max_tracks = int(max_tracks)
    except ValueError:
        # Return an error and set an appropriate status code
        return jsonify({'error': 'Bad Request',
                        'code': 400,
                        'message': 'Invalid parameter value for `max_tracks` - integer required'
                        }), 400
    
    # Everything seems fine, let's do it
    movie = get_movie(query)
    tracks = get_tracks(movie.title, max_tracks, as_dict = True)
    
    # Finally, return a big bunch of JSON
    return jsonify(movie = movie.__dict__,
                   tracks = tracks,
                   num_tracks = len(tracks))




# Error handler for non-existing resources
@app.errorhandler(404)
def page_not_found(error):
    if request.path.startswith("/api/"):
        # API requests should get JSON
        return jsonify({ 'error': 'Resource Not Found', 'code': 404, 'message': 'Requested endpoint does not exist' }), 404
    else:
        # Other requests should get HTML
        return render_template("error.html", code = 404, description = "Page not found"), 404



if __name__ == '__main__':
    app.debug = True
    app.run()
