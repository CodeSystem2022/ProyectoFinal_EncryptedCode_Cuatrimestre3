#Limachi Lucas - Codigo modificado para que sea ejecutable
import tkinter
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox as mb
import sqlite3
import matplotlib.pyplot as plt

# Clase principal de la ventana
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plataforma Uteniana")
        self.geometry("500x400")
        self.config(bg="white")

        self.create_menu()

        self.tabControl = tk.ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")

        # Primera pestaña: Registro
        self.tab1 = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Registro")
        RegistroVentana(self.tab1, self)
        label_example = tk.Label(self, text="Registro", bg="white", font=("Comic Sans MS", 16), fg="red")

        
    
        # Segunda pestaña: Actualizar
        self.tab2 = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="Actualizar")
        ActualizarVentana(self.tab2, self)

        # Tercera pestaña: Eliminar
        self.tab3 = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text="Eliminar")
        EliminarVentana(self.tab3, self)

    # Crear el menú
    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Salir", command=self.quit)

        data_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Datos", menu=data_menu)
        data_menu.add_command(label="Mostrar gráfico", command=self.plot_grafico)

    # Función para mostrar el gráfico
    def plot_grafico(self):
        # Conexión a la base de datos
        db = sqlite3.connect('Plataforma.db')
        c = db.cursor()
        c.execute("SELECT COUNT(*) FROM usuarios GROUP BY SUBSTR(Mail, INSTR(Mail, '@') + 1)")
        result = c.fetchall()
        db.close()

        dominios = [row[0] for row in result]
        etiquetas = [row[1] for row in result]

        # Crear y mostrar el gráfico
        plt.bar(etiquetas, dominios)
        plt.xlabel("Dominio")
        plt.ylabel("Cantidad")
        plt.title("Usuarios registrados por dominio de correo electrónico")
        plt.show()

# Clase de la ventana de registro
class RegistroVentana(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.config(bg="white")

        label_example = tk.Label(self, text="Registro", bg="white", font=("Comic Sans MS", 16))
        label_example.pack(side="top")

        labels = ["Legajo:", "Nombre:", "Apellido:", "Domicilio:", "Mail:"]
        self.entries = []

        # Crear etiquetas y campos de entrada
        for label_text in labels:
            label = tk.Label(self, text=label_text, bg="white", font=("Comic Sans MS", 10))
            label.pack()

            entry = tk.Entry(self)
            entry.pack()
            self.entries.append(entry)

        # Botón de registro
        button = tk.Button(self, text="Registrar", command=self.registro, bg="white", font=("Comic Sans MS", 10))
        button.pack(side="bottom")

        self.main_window = main_window

    # Función de registro
    def registro(self):
        values = [entry.get() for entry in self.entries]

        if all(values):
            # Conexión a la base de datos y registro del usuario
            db = sqlite3.connect('Plataforma.db')
            c = db.cursor()
            c.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?)", tuple(values))
            db.commit()
            db.close()

            # Mostrar mensaje de registro exitoso
            mb.showinfo(title="Registro Correcto", message="Su registro fue exitoso.")
            self.main_window.focus_set()
            self.destroy()
            self.main_window.plot_grafico()
        else:
            # Mostrar mensaje de error si no se completaron todos los campos
            mb.showerror(title="Error", message="Por favor, complete todos los campos.")

# Clase de la ventana de actualización
class ActualizarVentana(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.config(bg="white")

        label_example = tk.Label(self, text="Actualizar", bg="white", font=("Comic Sans MS", 16))
        label_example.pack(side="top")

        labels = ["Legajo:", "Nombre:", "Apellido:", "Domicilio:", "Mail:"]
        self.entries = []

        # Crear etiquetas y campos de entrada
        for label_text in labels:
            label = tk.Label(self, text=label_text, bg="white", font=("Comic Sans MS", 10))
            label.pack()

            entry = tk.Entry(self)
            entry.pack()
            self.entries.append(entry)

        # Botón de actualización
        button = tk.Button(self, text="Actualizar", command=self.act, bg="white", font=("Comic Sans MS", 10))
        button.pack(side="bottom")

        self.main_window = main_window

    # Función de actualización
    def act(self):
        values = [entry.get() for entry in self.entries]

        if all(values):
            # Conexión a la base de datos y actualización del usuario
            db = sqlite3.connect('Plataforma.db')
            c = db.cursor()
            c.execute("UPDATE usuarios SET Nombre=?, Apellido=?, Domicilio=?, Mail=? WHERE Legajo=?", tuple(values))
            db.commit()
            db.close()

            # Mostrar mensaje de actualización exitosa
            mb.showinfo(title="Actualización Correcta", message="Su actualización fue realizada.")
            self.main_window.focus_set()
            self.destroy()
        else:
            # Mostrar mensaje de error si no se completaron todos los campos
            mb.showerror(title="Error", message="Por favor, complete todos los campos.")

# Clase de la ventana de eliminación
class EliminarVentana(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.config(bg="white")

        label_example = tk.Label(self, text="Eliminación", bg="white", font=("Comic Sans MS", 16))
        label_example.pack(side="top")

        label = tk.Label(self, text="Legajo:", bg="white", font=("Comic Sans MS", 10))
        label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        # Botón de eliminación
        button = tk.Button(self, text="Eliminar", command=self.eliminar, bg="white", font=("Comic Sans MS", 10))
        button.pack(side="bottom")

        self.main_window = main_window

    # Función de eliminación
    def eliminar(self):
        legajo = self.entry.get()

        if legajo:
            # Conexión a la base de datos y eliminación del usuario
            db = sqlite3.connect('Plataforma.db')
            c = db.cursor()
            c.execute("DELETE FROM usuarios WHERE Legajo=?", (legajo,))
            db.commit()
            db.close()

            # Mostrar mensaje de eliminación exitosa
            mb.showinfo(title="Eliminación Correcta", message="El usuario ha sido eliminado.")
            self.main_window.focus_set()
            self.destroy()
        else:
            # Mostrar mensaje de error si no se ingresó un legajo válido
            mb.showerror(title="Error", message="Por favor, ingrese un legajo válido.")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
