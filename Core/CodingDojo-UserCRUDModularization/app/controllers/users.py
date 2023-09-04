from flask import Flask, render_template, request, redirect
from app import app
from app.models.user import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("leer(todo).html",all_users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("crear.html")

@app.route('/add_user',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))


@app.route('/edit_user',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')
