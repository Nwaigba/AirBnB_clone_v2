#!/usr/bin/python3
""" A script that Starts a flask web app
your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_flask():
    """Return string when route queried
    """
    return render_template("10-hbnb_filters.html")

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=None)
