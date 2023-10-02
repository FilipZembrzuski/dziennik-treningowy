from flask import Flask, render_template, redirect, request, url_for
import sqlite3 as sql
import database

app = Flask(__name__)

def add_prop():
    conn = sql.connect("training'sDictionary.db")
    
    conn.execute("Insert Into 'proportions'(`date`, `height`, `knee`, `elbow`, `crimson`, `shoulder`, `chest`, `arm`, `calf`, `thigh`, `forearm`, `neck`) values ()")

@app.route("/home")
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/calculator", methods = ["POST","GET"])
def calc():
    return render_template("calculator.html")

@app.route("/addProportions", methods = ["POST"])
def addprop():
    if request.method == "POST":
        fnames = request.form
        prop = []
        
        for n in fnames:
            a = request.form[n]
            prop.append(a)
            
        for i in prop:
            print(i)
        return redirect("/calculator")
    else:
        return redirect("/calculator")
    
@app.route("/dictionary")
def diction():
    return render_template("dictionary.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=420,debug=True)