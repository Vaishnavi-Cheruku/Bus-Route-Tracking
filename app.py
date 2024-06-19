from flask import Flask, request, render_template
from data import ROUTES

app = Flask(__name__)

@app.route("/")
def route_tracking():
    return render_template('login.html', routes=ROUTES)

@app.route("/login.html")
def login():
    return render_template('login.html', routes=ROUTES)

@app.route("/home.html")
def home():
    return render_template('home.html', routes=ROUTES)

@app.route("/logout.html")
def logout():
    return render_template('logout.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/routee.html")
def routee():
    return render_template('routee.html', routes=ROUTES)

@app.route("/feed.html")
def feedback():
    return render_template('feed.html')

@app.route("/profile.html")
def profile_page():
    return render_template('profile.html')

@app.route("/tracking.html")
def tracking():
    return render_template('tracking.html')

@app.route("/search.html")
def search_page():
    return render_template('search.html')

@app.route("/search", methods=['POST'])
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)