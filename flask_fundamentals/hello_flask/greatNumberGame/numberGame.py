import random
from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'randomNumberGame'

@app.route('/')
def homescreen():
    if 'winner' in session:
        compare=int(session['playtime'])
        medal=int(session['winner'])
        if 'playtime' in session:
            if(compare>medal):
                phrase="Too high!"
            elif(medal>compare):
                phrase="Too low!"
            elif(medal==compare):
                return render_template('winner.html')
            return render_template('loser.html', phrase=phrase)
        else:
            session['playtime']=50
            return redirect('/play')
    else:
        session['winner']=random.randrange(0,101)
        session['playtime']=random.randrange(0,101)
        print(session['winner'])
        print(session['playtime'])
        return render_template('homescreen.html')

@app.route('/play', methods=['POST'])
def play():
    session['playtime']=request.form['playtime']
    print(request.form)
    return redirect('/')

@app.route('/clear', methods=['POST','GET'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)