
from turtle import home
from flask import Flask, request, render_template 

import joblib

app = Flask(__name__)   
  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "GET":
        
        return render_template("home.html")
    else:
       
       request.method == "POST"
       
       
       age = request.form.get("age")
       
       weight = request.form.get("weight") 

       model  = joblib.load('regr.pkl')

       predicted_value = model.predict([[age,weight]])
       
       return render_template("home.html",value=predicted_value[0])
  
if __name__=='__main__':
   app.run()