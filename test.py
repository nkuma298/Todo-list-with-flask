from flask import Flask, render_template, request, redirect, session, g, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
    #return "<p>Hello, World!</p>"

@app.route("/show")
def show():
    return "<p>This is product page</p>"

@app.route("/products")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<p>This is product page</p>"

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('hello_world'))
        
    return render_template('login.html')

@app.route('/protected')
def protected(): 
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']



if __name__ == "__main__":
    app.run(debug=True)
