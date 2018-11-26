import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "shhh"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'money' not in session:
        session['money']=0
        


    return render_template('ninjagold.html', goldVal=session['gold'], money=session['money'])


@app.route('/process_money', methods=['POST'])
def money():
    if request.form['type']=='farm':
        session['money'] += random.randrange(10, 20)
        session['gold'] += session['money']

    elif request.form['type']=='cave':
        session['money'] += random.randrange(5, 10)
        session['gold'] += session['money']
    elif request.form['type']=='house':
        session['money'] += random.randrange(2, 5)
        session['gold'] += session['money']
    elif request.form['type']=='casino':
        session['money'] += random.randrange(-50, 50)
        session['gold'] += session['money']
    elif request.form['type']=='zero':
        session.clear()
    
    


    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)