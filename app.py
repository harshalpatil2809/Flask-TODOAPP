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
    tasks.append({'task':task, 'time':time, 'date':date, 'completed':False})
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:index>", methods=['POST'])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return render_template("index.html",tasks = tasks )

@app.route("/toggle/<int:index>", methods=['POST'])
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = not tasks[index]['completed']
    return render_template("index.html",tasks = tasks )

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")