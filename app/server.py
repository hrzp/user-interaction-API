from flask import make_response, abort
import connexion

# Create the application instance
app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={"swagger_ui": True}
)

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        Interface url
    """
    resp = """<a href='/api/ui'>API Interface</a>"""
    return make_response(resp, 200)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
