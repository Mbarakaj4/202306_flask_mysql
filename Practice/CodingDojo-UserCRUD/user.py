# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['idUsuarios']
        self.first_name = data['Nombre']
        self.last_name = data['Apellido']
        self.email = data['Correo_Electronico']
        self.created_at = data['Created_at']
        self.updated_at = data['Updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (Nombre,Apellido,Correo_Electronico) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        result = connectToMySQL('users_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM usuarios WHERE idUsuarios = %(id)s";
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE usuarios SET Nombre=%(fname)s,Apellido=%(lname)s,Correo_Electronico=%(email)s,Updated_at=NOW() WHERE idUsuarios = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM usuarios WHERE idUsuarios = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)