from flask import Flask, render_template, redirect, request
import sqlite3 as sql
import database
import datetime as dt

app = Flask(__name__)

def read_prop_cols():
    conn = sql.connect("training'sDictionary.db")
    propNames = conn.execute("Select name from propCol")
    conn.commit()
    
    pn = []
    
    for i in propNames:
        pn.append(i[0])
        
    return(pn)
    
def read_prop():
    conn = sql.connect("training'sDictionary.db")
    prop = conn.execute("Select * From 'proportions' Order by `date` desc")
    conn.commit()
    
    pn = read_prop_cols()
    proportions = []

    for i in prop:
        zmk = 0
        for a in pn: 
            if zmk == 0:
                props = {
                    'id': i[zmk]
                }
                
                zmk += 1
            props[a] = i[zmk]
            zmk += 1
        proportions.append(props)
    return(proportions)
   
def add_prop(*proportions):
    conn = sql.connect("training'sDictionary.db")
    propNames = conn.execute("Select name from propCol")
    conn.commit()
        
    query = "Insert Into 'proportions'("
    add = ""
    for i in propNames:
        query = (f"{query}{add}'{i[0]}'")
        add = ", "
        
    query = (f"{query}) values(")
    add = ""
    for i in proportions:
        try:
            index = i.index("-")
            query = (f"{query}{add}'{i}'")
        except:
            query = (f"{query}{add}{i}")
            
        add = ", "
    query = query + ")"
    conn.execute(query)
    conn.commit()
    conn.close()

def update_prop(id, *proportions):
    conn = sql.connect("training'sDictionary.db")
    propNames = conn.execute("Select name from propCol")
    conn.commit()
        
    
    
    propN = []
    for i in propNames:
        propN.append(i[0])
    
    query = "UPDATE `proportions` SET  "
    add = ""
    a = 0
    for i in proportions:
        try:
            index = i.index("-")
            query = (f"{query}{add}`{propN[a]}` = '{i}'")
        except:
            query = (f"{query}{add}`{propN[a]}` = {i}")
            
        add = ", "
        a += 1
    query = (f"{query} WHERE `id` = {id}")
    print(query)
    conn.execute(query)
    conn.commit()
    conn.close()
 
@app.route("/home")
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/calculator", methods = ["POST","GET"])
def calc():
    datetime = dt.datetime.now().strftime("%Y-%m-%d")
    prop = read_prop()
    pn = read_prop_cols()
    
    return render_template("calculator.html", prop = prop, pn = pn, datetime = datetime)

@app.route("/addProportions", methods = ["POST"])
def addprop():
    if request.method == "POST":
        fnames = request.form
        prop = []
        
        for n in fnames:
            a = request.form[n]
            prop.append(a)
        
        
        add_prop(*prop)
        return redirect("/calculator")
    else:
        return redirect("/calculator")
    
@app.route("/dictionary")
def diction():
    return render_template("dictionary.html")

@app.route("/updateProportions", methods = ["GET"])
def updateprop():
    if request.method == "GET":
        udata = request.args
        prop = []
        
        for n in udata:
            a = request.args[n]
            if n != "id":
                prop = a.split(",")
            else:
                id = a
        
        update_prop(id, *prop)
        return redirect("/calculator")
    else:
        return redirect("/calculator")
   
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=420,debug=True)