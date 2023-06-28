#Lucas Limachi - se realizo un grafico con datos de estudiantes
import matplotlib.pyplot as plt
import numpy as np

# Datos de los estudiantes
nombres = ['Ana Perez', 'Sofia Cruz', 'Kevin Gomez', 'Alan Rodriguez', 'Mariana Ruiz',
           'Jose Quinteros', 'Belen Pereyra', 'Angel Martinez', 'Sergio Nuñez', 'Martina Toledo', 'Joaquina Zarate']
calificaciones = [8.5, 9.0, 7.2, 8.8, 9.5, 7.9, 8.0, 7.6, 8.3, 9.1, 9.6]

# Crear un arreglo con los índices de los estudiantes
indices = np.arange(len(nombres))

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(8, 5))

# Graficar los datos de los estudiantes
ax.bar(indices, calificaciones)

# Configurar las etiquetas del eje x
ax.set_xticks(indices)
ax.set_xticklabels(nombres, rotation=45, ha='right')

# Configurar el título y los nombres de los ejes
ax.set_title('Calificaciones Finales Promedio de Carrera')
ax.set_xlabel('Estudiantes')
ax.set_ylabel('Calificaciones')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
