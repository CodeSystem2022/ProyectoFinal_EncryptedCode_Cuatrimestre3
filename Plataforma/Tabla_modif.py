#ROCIO PULITTA: Se realizo la carga de datos en la BD
import sqlite3

conn = sqlite3.connect('Plataforma.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS usuarios(Legajo INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT, Domicilio TEXT, Mail TEXT)")

create_table()

# Insertar datos en la tabla

# Definir la clase 'usuarios' como una tupla en lugar de una llamada de función
usuario1 = (1111, 'ana', 'Perez', 'Avellaneda N56', 'aperez@mail.com')
usuario2 = (2222, 'Sofia', 'Cruz', 'Independencia N° 589', 'scruz@mail.com')
usuario3 = (3333, 'Kevin', 'Gomez', 'San Martin N° 150', 'kgomez@mail.com')
usuario4 = (4444, 'Alan', 'Rodriguez', '9 de Julio N° 650', 'arodr@mail.com')
usuario5 = (5555, 'Mariana', 'Ruiz', '25 de Mayo N° 1580', 'mruiz@mail.com')
usuario6 = (6666, 'Jose', 'Quienteros', 'Pueyrredon N° 456', 'jquinteros@mail.com')
usuario7 = (7777, 'Belen', 'Pereyra', 'Tucuman N°890 ', 'bpereyra@mail.com')
usuario8 = (8888, 'Angel', 'Martinez', 'Buenos Aires N° 998', 'amartinez@mail.com')
usuario9 = (9999, 'Sergio', 'Nuñez', 'Mitre N°85 ', 'snoñez@mail.com')
usuario10 = (1010, 'Martina', 'Toledo', 'Jujuy N° 1246', 'mtoledo@mail.com')
usuario11 = (1212, 'Joaquina', 'Zarate', 'Salta N° 510', 'jzarate@mail.com')

#  Insertar los datos de los usuarios utilizando el comando executemany
c.executemany("INSERT INTO usuarios VALUES (?,?,?,?,?)", [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10, usuario11])
conn.commit()

# Seleccionar y mostrar todos los usuarios de la tabla
c.execute("SELECT * FROM usuarios")
usuarios = c.fetchall()
print(usuarios)

# Cerrar la conexión
conn.close()
