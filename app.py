from flask import Flask, request, jsonify
import csv
import pandas as pd

allMovies = []
likedMovies = []
notLikedMovies = []
didNotWatchMovies = []

# with open('movies.csv') as f:
#     reader = csv.reader(f)

#     df = list(reader)
#     allMovies = df[1:]

df = pd.read_csv('movies.csv')
allMovies = list(df)
allMovies = allMovies[1:]

app = Flask(__name__)

@app.route('/get-movie')

def getMovie():
    return jsonify({
        'data': allMovies[1:],
        'message': 'success'
    })

@app.route('/liked-movies', methods = ['POST'])

def likedMovie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)

    return jsonify({
        'message': 'success'
    })

@app.route('/unliked-movies', methods = ['POST'])

def unlikedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    notLikedMovies.append(movie)

    return jsonify({
        'message': 'success'
    })

@app.route('/did-not-watch', methods = ['POST'])

def didNotWatch():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    didNotWatchMovies.append(movie)

    return jsonify({
        'message': 'sucess'
    })

if(__name__ == '__main__'):
    app.run()