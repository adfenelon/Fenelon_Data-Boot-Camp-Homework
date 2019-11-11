# create a server, import Flask
from flask import Flask, render_template

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Define routes

@app.route("/")
@app.route("/home")
@app.route("/Max_Temp")
@app.route("/Humidity")
@app.route("/Cloudiness")
@app.route("/Wind_Speed")
@app.route("/Comparison")
@app.route("/WData")


# Define what to do when a user hits the index route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/Max_Temp")
def Max_Temp(): 
    return render_template('maxtemp.html')

@app.route("/Humidity")
def Hunidity():   
    return render_template('humudity.html')

@app.route("/Cloudiness")
def Cloudiness():
    return render_template('cloudiness.html')

@app.route("/Wind_Speed")
def Wind_Speed():   
    return render_template('wind_speed.html')

@app.route("/Comparison")
def Comparison():  
    return render_template('compare.html')

@app.route("/WDataset")
def WDataset():
    return render_template('dataset.html')

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
 #   TEMPLATE_AUTO_RELOAD = True
 #   app_secret_key = 'super_secret_key'
    
