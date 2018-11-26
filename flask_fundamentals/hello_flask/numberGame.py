from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random 


@app.route('/') 
def index():
    session['count']=random.randrange(0,101)
    if session['formData'] != None:
        if int(session['formData'])>session['count']:
            print('toohigh')
            result='toohigh'
        if int(session['formData'])<session['count']:
            print('toolow')
            result='low'

    
    
    return render_template("numberGame.html",result=result)

@app.route('/users', methods=['POST']) 
def create():
    session['formData']=int(request.form['number'])
    
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True) 