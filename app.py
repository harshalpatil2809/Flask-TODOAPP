from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return render_template("result.html", message = message, name=name)

if __name__ == "__main__":
    app.run()