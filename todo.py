from flask import Flask, render_template, request

app = Flask(__name__)

todolist=['Do youtube','Get money']



@app.route('/', methods= ['GET','POST'] )
def index():
    new_todo = request.form["new_todo"]
    todolist.append(new_todo)
    return render_template("todo.html.jinja", my_todos=todolist)
