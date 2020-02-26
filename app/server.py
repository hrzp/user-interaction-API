
"""
It is our file server that has the task of setting up the API.
The approach of the structure is a package base.
We have an app directory that contains our project files.
use of package model gives us some benefits for
working with nested files and modules without dependency injection.

The swagger.yml file links the routes to our functions that are placed in the views directory.

for responding to the user requests we use a Response class
that provides a modular structure. It is based on utils.response_handler.py
"""

from flask import make_response, abort
import connexion


# Create the application instance
app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={"swagger_ui": True}
)

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml', strict_validation=True)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser URL
    :url localhost:5000/
    :return:        Interface url
    """
    resp = """<a href='/api/ui'>API Interface</a>"""
    return make_response(resp, 200)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
