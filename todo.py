from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todolist=['Do youtube','Get money']



@app.route('/', methods= ['GET','POST'] )
def index():
    if request.method == 'POST':
     new_todo = request.form["new_todo"]
     todolist.append(new_todo)
   
    return render_template("todo.html.jinja", my_todos=todolist)


@app.route('/delete_todolist/<int:todo_index>', methods= ['POST'])
def todo_delete(todo_index):
   del todolist[todo_index]

   return redirect('/')
