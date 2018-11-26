from flask import Flask, render_template, request, redirect   # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.


@app.route('/') 
def index():
    return render_template("dojoSurvey.html")

@app.route('/users', methods=['POST']) 
def create():
    return render_template("created.html")

@app.route('/danger') 
def danger():
    print('Redirected Back to "/"')
    return render_template("dojoSurvey.html")
    



if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode