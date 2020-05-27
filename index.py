from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def inicio():
    return render_template("index.html")

@app.route("/mgrafico")
def fnMGrafico():
    return ("<h1>Hola mundo x2</h1>")

if __name__ == "__main__":
    app.run(debug=True)
