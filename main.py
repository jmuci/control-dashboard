from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Welcome to Hello World! </h1>"

@app.route("/foo")
def foo():
    return "<h2> This is a foo page! </h2>"

@app.route("/user/<username>")
def show_user_profile(username=None):
#    return 'User %s' % username
    return render_template('show_user_profile.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login')
def login(): pass

#with app.test_request_context():
#    print url_for('login')

if __name__ == "__main__":
        app.debug = True
        app.run()
