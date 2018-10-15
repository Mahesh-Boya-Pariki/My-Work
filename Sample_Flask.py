from flask import Flask, request, jsonify, redirect, url_for

app=Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/profile')
def profile():
    return "admin"


@app.route('/guest/<name>')
def guest(name):
    return "Hi %s"% name


@app.route('/post/<int:id>')
def post(id):
    return "Id is %s"%id


@app.route('/user/<username>')
def user(username):
    if username == 'profile':
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('guest', name=username))

@app.route('/process',methods=['GET','POST'])
def process():
    value = request.json["name"]
    return jsonify({"key":value})

app.run( debug=True)


