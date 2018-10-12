from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"


@app.route('/profile,<user>')
def profile(user):
    return "Hello %s" % user


app.run(debug=True)
