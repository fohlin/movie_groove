# Movie Groove

_Movie Groove_ is an example mashup app, written in Python using [Flask](http://flask.pocoo.org). It shows the main concepts of routing, templates, and making external API calls. It is not, however, written in a robust way. Notably, a good app should intelligently handle API errors, timeouts, etc.

## Running it

### Getting Flask

The [Flask installation guide](http://flask.pocoo.org/docs/0.10/installation/) is quite good. It recommends learning and using _virtualenv_ to create a seperate Python environment for each project -- which is handy.

You can also install Flask (and any other Python package) globally, using the _pip_ package manager. If you're on Python 2.7.9, you already have pip. Then you can do this on the command line:

    sudo python -m pip install flask

Otherwise, [install pip](https://pip.readthedocs.org/en/stable/installing.html) serparately, and run:

    sudo pip install flask

This project also includes a `requirements.txt` file, so you could:

    cd PATH_TO_THIS_PROJECT
    sudo pip install -r requirements.txt


### Starting the app

Just run `movie_groove/app.py`!


## See also

- [The Flask Documentation](http://flask.pocoo.org/docs/0.10/)
- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

