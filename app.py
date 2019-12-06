from flask import (
    Flask,
    render_template,
    request,
)
from flask_cors import CORS

from flask.json import JSONEncoder
from datetime import date

from api.router import *


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            if isinstance(obj, time):
                return obj.isoformat()
            
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


# Create the application instance
app = Flask(__name__, template_folder="templates")
app.json_encoder = CustomJSONEncoder

CORS(app)

# Create a URL route in our application for "/"
@app.route('/')
def api_home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/api/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/api/<path:path>', methods=['GET', 'POST'])
def api_catch_all(path):
    if request.method == "GET":
        return route(path, request.method, request.args)
    if request.method == "POST":
        if request.mimetype in ['application/x-www-form-urlencoded',  'multipart/form-data']:
            return route(path, request.method, request.form)
        if request.mimetype == 'application/json':
            return route(path, request.method, request.json)
        else:
            pass
    


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)