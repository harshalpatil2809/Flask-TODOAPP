from flask import Flask,render_template,request

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html",tasks = tasks)

@app.route("/add", methods=['POST'])
def submit():
    task = request.form['task']
    date = request.form['date']
    time = request.form['time']
    tasks.append({'task':task, 'time':time, 'date':date})
    return render_template("index.html", tasks=tasks)


@app.route("/delete")
def delete():
    task = request.form['task']
    date = request.form['date']
    time = request.form['time']
    tasks.remove({'task':task, 'time':time, 'date':date})
    return render_template("index.html")



if __name__ == "__main__":
    app.run()