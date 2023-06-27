#Andrea Llavel. Este Grafico es para cargar los datos de estudiantes y para poder ver una manera de como se hacen
import matplotlib.pyplot as plt    #Matplotlib: libreria ,cuyo objetivo es visualizar las señales electricas del cerebro de personas epilepticas.Desarrollado por un Biologo
# Para conseguirlo, queria replicar las funcionalidades de creacion grafica de MATLAB con Python
from mpl_toolkits.mplot3d import Axes3D  #Es el contenedor de la grafica.Una figura puede contener varios axes y un axes puede contener varias graficas
import numpy as np     #Numpy: Numerical Python.Se utiliza para programacion cientifica ,la ingenieria y las matemiaticas o la ciencia
from numpy import *
fig = plt.figure(figsize = (8, 5))
  # Creamos una figura
ax1 = fig.add_subplot(111, projection='3d')   #Creamos un Eje

x3 = [1,2,3,4,5,6,7,8,9,10] #Se crea un arreglo con datos
y3 = [5,6,7,8,2,5,6,3,7,2]  # En una lista
z3 = np.zeros(10)           #Se crea unaMatriz
# Datos a la superficie en 3D
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]
# graficar la superfie en 3D
surface= ax1.bar3d(x3 , y3 , z3, dx, dy, dz,  cmap = "coolwarm")
fig.colorbar(surface)
# Mostrar el Grafico
plt.show()
