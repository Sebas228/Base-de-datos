import sqlite3

# Conectarse a la base de datos (se creará si no existe)
conexion = sqlite3.connect('basededatos.db')

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Crear una tabla en la base de datos
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   edad INTEGER NOT NULL)''')

# Insertar datos en la tabla
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 25))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('María', 30))
conexion.commit()

# Consultar los datos de la tabla
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Imprimir los datos obtenidos
for usuario in usuarios:
    print("ID:", usuario[0])
    print("Nombre:", usuario[1])
    print("Edad:", usuario[2])
    print("")

# Cerrar la conexión y el cursor
cursor.close()
conexion.close()
