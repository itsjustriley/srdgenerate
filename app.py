"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, redirect, render_template
import sample
import rearrange
import histogram
import random
import twitter 
import markov
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
def source_text():
    with open('dnd5esrd.txt', 'r') as f:
        return f.read().replace('\n', ' ')
        
source = source_text()

new_histogram = histogram.histogram(source)

words = source.split()
words = [word.strip() for word in words if word.strip()]
words = [words[i] + words[i+1] if words[i+1] in [',', '.', '!', '?', ';', ':'] else words[i] for i in range(len(words)-1)]
words = [word for word in words if word not in [',', '.', '!', '?', ';', ':']]

@app.route("/")
def home():
    sentence = markov.MarkovChain(words).generate_sentence()
    return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')
    


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
    To learn more about Flask's DEBUG mode, visit
    https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True, host='0.0.0.0', port=5000)