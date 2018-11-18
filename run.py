import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Home page requesting username with rules displayed to the user '''
    if request.method == 'POST':
        return redirect(request.form['username'])
    return render_template('index.html')

@app.route('/<username>')
def user(username):
    ''' User directed to the welcome page to pick thier challange '''
    return render_template('user.html', username=username)
    
app.run(os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)