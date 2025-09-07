from flask import Flask,render_template,request

app = Flask(__name__, template_folder="./templates",static_folder="./static")

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


@app.route("/delete/<int:index>", methods=['POST'])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return render_template("index.html",tasks = tasks )


def handler(environ, start_response):
    return app(environ, start_response)
