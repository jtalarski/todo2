from flask import Flask, render_template, request, redirect, url_for
import psycopg2
# import psycopg2.extras
from connecting import con
app = Flask(__name__)

@app.route('/')
def index():
   # here is a poor attempt
   cur = con.cursor()
   cur.execute('SELECT * FROM tasks')
   rows = cur.fetchall()
   print(rows)
   return render_template('base.html', rows=rows)
   

@app.route("/add", methods=['POST'])
def add():
    task = request.form.get("task")
    querytext = 'INSERT INTO tasks ("task") VALUES (%s);'
    cur = con.cursor()
    cur.execute(querytext, [task])
    con.commit()
    return redirect(url_for("index"))
    con.close()
    

@app.route("/update/<int:id>")
def update(id):
    querytext = 'UPDATE "tasks" SET "status" = TRUE WHERE "id" = %s;'
    # print(todo)
    todo = id
    cur = con.cursor()
    cur.execute(querytext, [todo])
    con.commit()
    # con.close() 
    return redirect(url_for("index")) 

@app.route("/delete/<int:id>")
def delete(id):
    todo = id
    querytext = 'DELETE FROM "tasks" WHERE "id" = %s;'
    cur = con.cursor()
    cur.execute(querytext, [todo])
    con.commit()
    # con.close()
    return redirect(url_for("index"))