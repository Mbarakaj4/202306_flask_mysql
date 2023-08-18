from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/users')

@app.route('/users/')
def index():
        users = User.get_all()
        return render_template("leer(todo).html", all_users = users)

@app.route('/users/new/')
def add_new() -> None:
    return render_template("crear.html")

@app.route('/add_user/', methods=["POST"])
def add_user():
    # print(request.form)
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    # Pasamos el diccionario de datos al método save de la clase User
    User.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/users/')

if __name__ == "__main__":
    app.run(debug=True)