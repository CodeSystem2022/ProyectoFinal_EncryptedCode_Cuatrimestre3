from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import sqlite3
import sys

# Configuración de la ventana principal

#Se crea la instancia de la ventana principal y se configuran sus propiedades
#como el título, tamaño, posición y fondo.

ventana = tk.Tk()
ventana.title("Plataforma Uteniana")
ventana.geometry("940x400+50+50")
ventana.config(bg="white")
ventana.iconbitmap(sys.executable)

# Conexión a la base de datos

#Se establece una conexión con la base de datos SQLite llamada 'Plataforma.db'.
#Se crea un cursor c que se utilizará para ejecutar consultas SQL en la base de datos.
db = sqlite3.connect('Plataforma.db')
c = db.cursor()

# Crear tabla "usuarios" si no existe

#Se ejecuta una consulta SQL para crear la tabla "usuarios" si no existe.
#La tabla tiene cinco columnas: "Nombre", "Valor", "Alumnos", "Lenguaje" y "Creador".
#La sentencia db.commit() se utiliza para confirmar los cambios en la base de datos.

c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (Nombre TEXT, Valor TEXT, Alumnos TEXT, Lenguaje TEXT, Creador TEXT)''')
db.commit()

# Muestra los usuarios almacenados en la base de datos

#Esta función realiza una consulta para seleccionar todos los registros de la tabla "usuarios".
#Los resultados se recuperan utilizando c.fetchall() y se almacenan en la variable usuarios.
#Luego, se itera sobre los registros y se imprime cada uno de ellos en la consola.

def mostrarUsuarios():
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    for usuario in usuarios:
        print(usuario)

# Muestra Ventana Registro

#Esta función crea una nueva ventana (Toplevel) cuando se llama.
#La nueva ventana se configura con un título, tamaño y fondo.
#A partir de aquí, se pueden agregar widgets y funcionalidades adicionales a la nueva ventana.

def nuevaVentana1():
    # Configuración ventana Registro
    newVentana = tk.Toplevel(ventana)
    newVentana.title("Registro de Usuario")
    newVentana.geometry("300x300+860+50")
    newVentana.config(bg="white")

    # Etiquetas
    labelExample = tk.Label(newVentana, text="Registro", bg="white", font=("Comic Sans MS", 16))
    labelExample.pack(side="top")  # Texto 'Registro'

    Label(newVentana, text="Nombre:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja3 = Entry(newVentana)
    caja3.pack()

    Label(newVentana, text="Valor:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja4 = Entry(newVentana)
    caja4.pack()

    Label(newVentana, text="Alumnos:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja5 = Entry(newVentana)
    caja5.pack()

    Label(newVentana, text="Lenguaje:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja6 = Entry(newVentana)
    caja6.pack()

    Label(newVentana, text="Creador:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja7 = Entry(newVentana)
    caja7.pack()

    # Función Registro
    
    #Esta función se llama cuando se hace clic en el botón "Registrar" en la ventana de registro.
    #Recupera los valores ingresados en las cajas de entrada (Entry) y los almacena en variables.
    #Luego, ejecuta una consulta SQL para insertar un nuevo registro en la tabla "usuarios" con los valores proporcionados.
    #Se utiliza db.commit() para confirmar los cambios en la base de datos.
    #Finalmente, se muestra un mensaje de información (messagebox) indicando que el registro fue exitoso.
    
    def registro():
        # Se toman variables por cada caja
        Nombre = caja3.get()
        Valor = caja4.get()
        Alumnos = caja5.get()
        Lenguaje = caja6.get()
        Creador = caja7.get()
        # El cursor actúa en la creación de cada registro
        c.execute("INSERT INTO usuarios values(?, ?, ?, ?, ?)", (Nombre, Valor, Alumnos, Lenguaje, Creador))
        db.commit()
        mb.showinfo(title="Registro Correcto", message="Su registro fue exitoso.")

    # Se crea un botón para habilitar la función "registro"
    buttons = tk.Button(newVentana, text="Registrar", command=registro, bg="green", fg="white", font=("Comic Sans MS", 10))
    buttons.pack(side="bottom", pady=10)

# Ventana Actualizar
def nuevaVentana2():
    # Configuración ventana Actualizar
    newVentana2 = tk.Toplevel(ventana)
    newVentana2.title("Actualización de Usuario")
    newVentana2.geometry("300x300+860+50")
    newVentana2.config(bg="white")

    # Etiquetas
    labelExample = tk.Label(newVentana2, text="Actualizar", bg="white", font=("Comic Sans MS", 16))
    labelExample.pack(side="top")  # Texto 'Actualizar'

    Label(newVentana2, text="Nombre:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja8 = Entry(newVentana2)
    caja8.pack()

    Label(newVentana2, text="Valor:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja9 = Entry(newVentana2)
    caja9.pack()

    Label(newVentana2, text="Alumnos:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja10 = Entry(newVentana2)
    caja10.pack()

    Label(newVentana2, text="Lenguaje:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja11 = Entry(newVentana2)
    caja11.pack()

    Label(newVentana2, text="Creador:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja12 = Entry(newVentana2)
    caja12.pack()

    # Función Actualizar
    def actualizar():
        # Se toman variables por cada caja
        Nombre = caja8.get()
        Valor = caja9.get()
        Alumnos = caja10.get()
        Lenguaje = caja11.get()
        Creador = caja12.get()
        # El cursor actúa en la actualización de cada registro
        c.execute("UPDATE usuarios SET Valor=?, Alumnos=?, Lenguaje=?, Creador=? WHERE Nombre=?", (Valor, Alumnos, Lenguaje, Creador, Nombre))
        db.commit()
        mb.showinfo(title="Actualización Correcta", message="La actualización fue exitosa.")

    # Se crea un botón para habilitar la función "actualizar"
    buttons2 = tk.Button(newVentana2, text="Actualizar", command=actualizar, bg="green", fg="white", font=("Comic Sans MS", 10))
    buttons2.pack(side="bottom", pady=10)

# Ventana Eliminar
def nuevaVentana3():
    # Configuración ventana Eliminar
    newVentana3 = tk.Toplevel(ventana)
    newVentana3.title("Eliminación de Usuario")
    newVentana3.geometry("300x150+860+50")
    newVentana3.config(bg="white")

    # Etiqueta
    labelExample = tk.Label(newVentana3, text="Eliminar", bg="white", font=("Comic Sans MS", 16))
    labelExample.pack(side="top")  # Texto 'Eliminar'

    Label(newVentana3, text="Nombre:", bg="white", font=("Comic Sans MS", 10)).pack()
    caja13 = Entry(newVentana3)
    caja13.pack()

    # Función Eliminar
    def eliminar():
    # Se toma la variable por la caja
        Nombre = caja13.get()
        print("Nombre a eliminar:", Nombre)  # Mensaje de depuración
    # El cursor actúa en la eliminación del registro
        c.execute("DELETE FROM usuarios WHERE Nombre=?", (Nombre,))
        db.commit()
        mb.showinfo(title="Eliminación Correcta", message="La eliminación fue exitosa.")


    # Se crea un botón para habilitar la función "eliminar"
    buttons3 = tk.Button(newVentana3, text="Eliminar", command=eliminar, bg="green", fg="white", font=("Comic Sans MS", 10))
    buttons3.pack(side="bottom", pady=10)

# Se crean botones para cada función

#Se crean varios botones en la ventana principal utilizando la clase Button de Tkinter.
#Cada botón tiene un texto, una función asociada (que se ejecuta cuando se hace clic en el botón), un color de fondo y un color de texto.
#Los botones se empaquetan en la ventana principal utilizando el método pack().

buttons = tk.Button(ventana, text="Mostrar Usuarios", command=mostrarUsuarios, bg="green", fg="white", font=("Comic Sans MS", 10))
buttons.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

buttons1 = tk.Button(ventana, text="Insertar Usuario", command=nuevaVentana1, bg="green", fg="white", font=("Comic Sans MS", 10))
buttons1.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

buttons2 = tk.Button(ventana, text="Actualizar Usuario", command=nuevaVentana2, bg="green", fg="white", font=("Comic Sans MS", 10))
buttons2.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

buttons3 = tk.Button(ventana, text="Eliminar Usuario", command=nuevaVentana3, bg="green", fg="white", font=("Comic Sans MS", 10))
buttons3.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Se ejecuta la ventana principal

#Este código se encarga de ejecutar el bucle principal de la aplicación y mantener la ventana abierta hasta que se cierre.

ventana.mainloop()

