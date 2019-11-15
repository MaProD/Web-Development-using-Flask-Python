# import the flask module.
from flask import Flask, render_template 
app = Flask(__name__) 
# A decolator to give more features to the route function
@app.route("/") 
def index(): 
   return render_template("index.html") 
#condition to auto debug only for development server
if __name__ == '__main__': 
   app.run(debug = True)
