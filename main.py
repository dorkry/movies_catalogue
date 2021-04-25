#main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [{"title": "Anioły i demony", "source": "static\\anioly_demony.jpg"}, {"title":"Hobbit. Niezwykła podróż", "source": "static\\hobbit.jpg"}, {"title":"Inferno", "source":"static\\inferno.jpg"}]
    return render_template("homepage.html", movies = movies)



