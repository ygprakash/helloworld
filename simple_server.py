from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'hello world, Bravilor Bonamat!!'

@app.route('/tri')
def ri_tech():
    """Print 'Hello, world!' as the response body."""
    return 'Bingoooooooooooo.  2nd page of Bravilor Bonamat!!!!!'

# @app.route('/batch')
# def batch():
#     """Print 'Hello, world!' as the response body."""
#     return 'feb-batch'


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")
