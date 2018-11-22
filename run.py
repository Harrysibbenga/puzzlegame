import os
import json
from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)
app.secret_key = "some_secret"

leaderboard = []

def write_to_file(filename, data):
    ''' Writelines to a specific filename '''
    with open(filename, 'a') as file:
        file.writelines(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Home page requesting username with rules displayed to the user '''
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(session['username'])
    return render_template('index.html')


@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    ''' User directed to the challange page'''
    data = []
    with open('data/text.json', 'r') as json_file:
        data = json.load(json_file)
        
    riddle_id = 0
    
    # Used to create a session for each user so thier score can be updated and resused.
    user = session.get('user_data', {})
    # If no user is present the user is created using the username of the current session and the user starts with 20 points.
    if not user:
       user = {
           "name": username,
           "score": 20,
       }
    
    if request.method == 'POST':
        # Get riddle_id from the value of the hidden input
        riddle_id = int(request.form['riddle_id'])
        # Get user's answer from the input box
        user_answer = request.form['answer'].lower()
        # Compare the user's answer to the correct answer of the riddle
        if data[riddle_id]['answer'] == user_answer:
            # Correct answer
            # Go to next riddle
            riddle_id += 1
        else:
            # Incorrect answer
            user['score'] -= 1
    # Session is stored and updated in the user variable
    session['user_data'] = user
    
    if riddle_id >= 10 or user['score'] <= 0:
        # When the game is over user apanded to the leaderboard list to be used later.
        leaderboard.append(user)
        # When the game is over session is closed and reset
        session.pop('user_data', None)
        return render_template("game_over.html", username=username, leaderboard=leaderboard)
    
    return render_template('user.html', username=username, user_score=user['score'], riddle_data=data, riddle_id=riddle_id)
    
app.run(os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)