# importar los módulos
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time

# ---------------------------------------- FUNCIONES ----------------------------------------------------

# FECHA Y HORA
# Función para obtener la fecha y hora actual del sistema.
def obtener_fecha_actual():
    now = datetime.now()
    fecha_actual = now.strftime("%d/%m/%Y %H:%M:%S")
    return fecha_actual

# Función para actualizar el reloj
def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta_reloj.config(text=hora_actual)
    ventana.after(1000, actualizar_reloj)


# EMPLEADOS

def agregar_empleado():
    nuevo_empleado = entrada_nuevo_empleado.get()
    if nuevo_empleado:
        listbox_empleados['values'] = empleados
        listbox_empleados.set(nuevo_empleado)
        print("Nuevo empleado agregado:", nuevo_empleado)
    else:
        print("Por favor, ingrese el nombre del nuevo empleado.")

# Función para abrir la lista de empleados con scroll en una ventana modal
def abrir_lista_empleados():
    ventana_lista = tk.Toplevel(ventana)
    ventana_lista.title("Seleccionar Empleado")
    ventana_lista.geometry("300x200")
    
    scrollbar_lista = tk.Scrollbar(ventana_lista)
    scrollbar_lista.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox_empleados = tk.Listbox(ventana_lista, yscrollcommand=scrollbar_lista.set)
    for empleado in empleados:
        listbox_empleados.insert(tk.END, empleado)
    listbox_empleados.pack(fill=tk.BOTH, expand=True)
    
    scrollbar_lista.config(command=listbox_empleados.yview)

# Función para manejar la selección del Combobox
    def seleccionar_empleado(event):
        seleccion = listbox_empleados.curselection()
        if seleccion:
            seleccionado = listbox_empleados.get(seleccion)
            listbox_empleados.set(seleccionado)
        ventana_lista.destroy()
    
    listbox_empleados.bind('<<ListboxSelect>>', seleccionar_empleado)

# VER LISTA    
def ver_lista_completos():
    # Crear una nueva ventana para mostrar la lista completa de datos
    ventana_datos = tk.Toplevel() # Toplevel para abrir una nueva ventana.
    ventana_datos.title("Datos Completos")
    
# Función para manejar el registro de entrada/salida
def registrar_entrada_salida(accion):
    nombre_empleado = listbox_empleados.get()
    if nombre_empleado:
        mensaje = f"{nombre_empleado} ha registrado su {accion} a las {time.strftime("%d/%m/%Y %H:%M:%S")}"
        lista_registro.insert(tk.END, mensaje)
    else:
        mensaje_error.config(text="¡Seleccione o agregue un nuevo empleado!")

#AGREGAR
def agregar_elemento():
    # Aquí puedes agregar la lógica para añadir un elemento o realizar una acción al presionar el botón
    print("Elemento agregado")

#ELIMINAR
# Función para eliminar un empleado
def eliminar_empleado():
    ventana_eliminar = tk.Toplevel(ventana)
    ventana_eliminar.title("Eliminar Empleado")
    ventana_eliminar.geometry("300x300")
    
    label_eliminar = tk.Label(ventana_eliminar, text="Seleccione el empleado a eliminar:")
    label_eliminar.pack(pady=10)
    
    scrollbar_eliminar = tk.Scrollbar(ventana_eliminar)
    scrollbar_eliminar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox_eliminar = tk.Listbox(ventana_eliminar, yscrollcommand=scrollbar_eliminar.set)
    for empleado in empleados:
        listbox_eliminar.insert(tk.END, empleado)
    listbox_eliminar.pack(fill=tk.BOTH, expand=True)
    
    scrollbar_eliminar.config(command=listbox_eliminar.yview)
    
    def confirmar_eliminacion():
        seleccion = listbox_eliminar.curselection()
        if seleccion:
            empleado_a_eliminar = listbox_eliminar.get(seleccion)
            empleados.remove(empleado_a_eliminar)
            entrada_nuevo_empleado()
            ventana_eliminar.destroy()
    
    boton_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion)
    boton_confirmar.pack(pady=10)

def eliminar_elemento():
    # Aquí puedes agregar la lógica para eliminar un elemento o realizar una acción al presionar el botón
    print("Elemento eliminado")

# -------------------------------------   # INTERFAZ  -----------------------------------------------------


# crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de entradas y salidas del empleado") #título
ventana.geometry('600x600') # Dimensiones
ventana.configure(background="#2F4F4F")

# Obtener la fecha actual
fecha_actual = obtener_fecha_actual()

# Reloj
etiqueta_reloj = tk.Label(ventana, font='Arial',background="#2f4f4f",fg="white")
etiqueta_reloj.pack(pady=10)
actualizar_reloj()

# EMPLEADOS

# Lista de empleados (menú desplegable)
label_empleado = tk.Label(ventana, text="Seleccione su nombre dentro de la lista:", background="#2F4F4F", fg="white")
label_empleado.pack(pady=5)

# Lista de empleados
empleados = ["Santiago Scacciaferro", "Nancy Débora", "Carlos Floriani", "Mayra","María Fernanda", "Anahí Robledo", "Horacio Gutierrez"]

# Crear Combobox con la lista de empleados
listbox_empleados = ttk.Combobox(ventana, values= empleados)
listbox_empleados.current(0)  # Establecer el valor por defecto
listbox_empleados.pack(pady=10)

# label para agregar nuevo empleado.
label_empleado = tk.Label(ventana, text="En caso de que no exista el empleado, agregar su nombre y apellido", background="#2F4F4F", fg="white")
label_empleado.pack(pady=5)

# Campo de entrada para el nuevo empleado
entrada_nuevo_empleado = ttk.Entry(ventana)
entrada_nuevo_empleado.pack(pady=5)

# Botón para agregar el nuevo empleado
boton_agregar = ttk.Button(ventana, text="Agregar Nuevo Empleado", command=agregar_empleado)
boton_agregar.pack(pady=5)

# BOTONES
#Existen dos tipo tk y ttk (la segunda es la mas "nueva")
style = ttk.Style()
style.configure("TButton", foreground="black")  # Configurar el color del texto del botón.

# Boton entrada
boton_entrada = tk.Button(ventana, text="Entrada", command=lambda: registrar_entrada_salida("entrada"))
boton_entrada.place(x=40, y=50) # Dimensiones del boton.
boton_entrada.pack(side="top", anchor="center") # Ubicacion, en este caso arriba - centro.
boton_entrada.pack(pady=10)

# Boton salida
boton_salida = tk.Button(ventana, text="salida", command=lambda: registrar_entrada_salida("salida")) # Contenido del texo del boton.
boton_salida.place(x=40, y=50) # Dimensiones del boton.
boton_salida.pack(side="top", anchor="center") # Ubicacion, en este caso arriba - centro.
boton_salida.pack(pady=10)


# Botón de confirmación con estilo ttk
# Botón ttk para ver la lista completa de datos
boton_ver_datos = ttk.Button(ventana, text="Ver la lista Completos", command=ver_lista_completos)
boton_ver_datos.pack(pady=10)

# Etiqueta para mensajes de error
mensaje_error = tk.Label(ventana, text="", background="#2F4F4F", fg="red")
mensaje_error.pack(pady=5)

# Botón para eliminar empleado
boton_eliminar_empleado = tk.Button(ventana, text="Eliminar empleado", command=eliminar_empleado)
boton_eliminar_empleado.pack(pady=5)

# LISTA DE REGISTROS

# Lista de registros (con barra de desplazamiento)
frame_registro = tk.Frame(ventana)
frame_registro.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_registro)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_registro = tk.Listbox(frame_registro, yscrollcommand=scrollbar.set)
lista_registro.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lista_registro.yview)

ventana.mainloop() #bucle principal del programa, debe ser la última línea del código y es para ejecutar la ventana.

