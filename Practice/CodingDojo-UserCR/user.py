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
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users_schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de users
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de users con cls
        for user in results:
            users.append(cls(user))
        return users
    # método de clase para guardar a nuestro amigo en la base de datos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Usuarios ( Nombre , Apellido , Correo_Electronico , Created_at, Updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )