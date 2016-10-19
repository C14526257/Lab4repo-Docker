from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/")
@app.route('/post/80')
def post():
    return 'Post 80'

@app.route('/')
def index():
    return 'Index Page'

@app.route("/")
@app.route('/hello')
def hellow():
    return 'Hello'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == "__main__":
    app.run(host='0.0.0.0,port=8080', debug=True)
