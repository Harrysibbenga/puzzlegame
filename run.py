import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Home page requesting username with rules displayed to the user '''
    if request.method == 'POST':
        return redirect(request.form['username'])
    return render_template('index.html')
    
app.run(os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)