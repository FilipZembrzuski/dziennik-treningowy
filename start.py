from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/calculator")
def calc():
    return render_template("calculator.html")

@app.route("/dictionary")
def dict():
    return render_template("dictionary.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=420,debug=True)