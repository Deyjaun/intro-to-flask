from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print



app = Flask(__name__)

conn = pymysql.connect(
  database = "dlawrence_todos",
  user = "dlawrence",
  password = "244557575",
  host = "10.100.33.60",
  cursorclass=pymysql.cursors.DictCursor
)




todolist=['Do youtube','Get money']

@app.route('/', methods= ['GET','POST'] )
def index():
    if request.method == 'POST':
     new_todo = request.form["new_todo"]
     todolist.append(new_todo)
     cursor = conn.cursor()
     cursor.execute(f"INSERT INTO `todos`(`description`) VALUES ('{new_todo}')")
     cursor.close()
     conn.commit()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `todos`")

    results = cursor.fetchall()

    cursor.close()

    print(results)
   
    return render_template("todo.html.jinja", my_todos=results)




@app.route('/delete_todolist/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
   cursor = conn.cursor()
   cursor.execute(f"DELETE FROM `todos` WHERE id = {todo_index}")
   
   cursor.close()
   conn.commit()


   return redirect('/')

