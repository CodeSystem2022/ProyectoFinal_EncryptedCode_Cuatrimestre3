#ROCIO PULITTA: Se realizo la carga de datos en la BD
import sqlite3

conn = sqlite3.connect('Plataforma.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT, Apellido TEXT, Domicilio TEXT, Mail TEXT)")

create_table()

# Insertar datos en la tabla
#c.execute("INSERT INTO usuarios VALUES('Juan','Gimenez', 'Belgrano N° 1060', 'jgimenez@mail.com')")
#conn.commit()

# Corrección: Definir la clase 'usuarios' como una tupla en lugar de una llamada de función
usuario1 = ('ana', 'Perez', 'Avellaneda N56', 'aperez@mail.com')
usuario2 = ('Sofia', 'Cruz', 'Independencia N° 589', 'scruz@mail.com')
usuario3 = ('Kevin', 'Gomez', 'San Martin N° 150', 'kgomez@mail.com')
usuario4 = ('Alan', 'Rodriguez', '9 de Julio N° 650', 'arodr@mail.com')
usuario5 = ('Mariana', 'Ruiz', '25 de Mayo N° 1580', 'mruiz@mail.com')
usuario6 = ('Jose', 'Quienteros', 'Pueyrredon N° 456', 'jquinteros@mail.com')
usuario7 = ('Belen', 'Pereyra', 'Tucuman N°890 ', 'bpereyra@mail.com')
usuario8 = ('Angel', 'Martinez', 'Buenos Aires N° 998', 'amartinez@mail.com')
usuario9 = ('Sergio', 'Nuñez', 'Mitre N°85 ', 'snoñez@mail.com')
usuario10 = ('Martina', 'Toledo', 'Jujuy N° 1246', 'mtoledo@mail.com')
usuario11 = ('Joaquina', 'Zarate', 'Salta N° 510', 'jzarate@mail.com')

# Corrección: Insertar los datos de los usuarios utilizando el comando executemany
c.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10, usuario11])
conn.commit()

# Seleccionar y mostrar todos los usuarios de la tabla
c.execute("SELECT * FROM usuarios")
usuarios = c.fetchall()
print(usuarios)

# Cerrar la conexión
conn.close()
