from flask import (
    Flask, redirect, render_template, url_for, request
)
import os
import json
import requests

app = Flask(__name__, static_url_path="")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "msayak1269"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def degToCard(deg):
    if (deg > 11.25 and deg <= 33.75):
        return "NNE"
    elif(deg > 33.75 and deg <= 56.25): 
        return "ENE"
    elif(deg > 56.25 and deg <= 78.75) :
        return "E"
    elif (deg > 78.75 and deg <= 101.25): 
        return "ESE"
    elif (deg > 101.25 and deg <= 123.75): 
        return "ESE" 
    elif (deg > 123.75 and deg <= 146.25): 
        return "SE" 
    elif (deg > 146.25 and deg <= 168.75): 
        return "SSE"
    elif (deg > 168.75 and deg <= 191.25): 
        return "S"
    elif (deg > 191.25 and deg <= 213.75): 
        return "SSW"
    elif (deg > 213.75 and deg <= 236.25): 
        return "SW" 
    elif (deg > 236.25 and deg <= 258.75): 
        return "WSW"
    elif (deg > 258.75 and deg <= 281.25): 
        return "W"
    elif (deg > 281.25 and deg <= 303.75): 
        return "WNW"
    elif (deg > 303.75 and deg <= 326.25): 
        return "NW" 
    elif (deg > 326.25 and deg <= 348.75): 
        return "NNW" 
    else: 
        return "N"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/view", methods=["POST"])
def view():
    city = request.form.get("city")
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5c39ab70f75fdb32260439d294e3c56c&units=metric"

    data = requests.get(api_url).json()
    if data["cod"]==200 :
        tempInCel = data["main"]["temp"]
        tempInFar = round(((tempInCel * 9) / 5) + 32)
        temp = [tempInCel, tempInFar]
        windDirection = degToCard(data["wind"]["deg"])
        description = data["weather"][0]["description"].capitalize()   
        return render_template("view.html", data=data, temp=temp,windDirection = windDirection,description = description)
    else:
        return render_template("view.html",data=data)    


if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')


 
        
      
