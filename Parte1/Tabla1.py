# Practica de tabla Sqlite3
import sqlite3

conn=sqlite3.connect('Plataforma.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Valor INT ,Alumnos TEXT,Lenguaje TEXT, Creador TEXT)")
	conn.commit()
	c.close()
	conn.close()

create_table()