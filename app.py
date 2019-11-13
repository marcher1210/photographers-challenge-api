from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from flask.json import JSONEncoder
from datetime import date

from api.generator import *

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

# Create a URL route in our application for "/"
@app.route('/')
def api_home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/api/numbers')
def api_numbers():
    print(request.args)
    return jsonify(numbers(args = request.args))

@app.route('/api/dates')
def api_dates():
    print(request.args)
    return jsonify(dates(args = request.args))

@app.route('/api/times')
def api_times():
    print(request.args)
    return jsonify(times(args = request.args))

@app.route('/api/words')
def api_words():
    print(request.args)
    return jsonify(words(args = request.args))

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)