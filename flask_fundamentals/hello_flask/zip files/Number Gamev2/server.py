import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "shhh"

@app.route('/')
def index():
    
    session['number'] = random.randrange(1, 101)
    print(session['number'])
    return render_template('index.html', guess=0, number=session['number'])

@app.route('/compare', methods=['POST'])
def compare():
    guess = int(request.form['guess'])
    return render_template('index.html', number=session['number'])

if __name__ == '__main__':
    app.run(debug=True)






