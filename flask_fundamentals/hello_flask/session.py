from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'



@app.route('/') 
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("session.html")

    
@app.route('/2') 
def add2():
    session['count']+=1
    return redirect('/')

@app.route('/clear') 
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 