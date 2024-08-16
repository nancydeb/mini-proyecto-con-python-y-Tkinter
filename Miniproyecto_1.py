import tkinter as tk
from tkinter import ttk
from tkinter import*
import time
from datetime import datetime

from tkinter import PhotoImage


# Crear la ventana de portada
ventana_portada = tk.Tk()
ventana_portada.title("Bienvenido al Sistema de Registro de Entradas y Salidas")
ventana_portada.geometry("600x600")
ventana_portada.config(bg="#808000")
# Etiqueta de bienvenida al iniciar la app.
label_bienvenida = tk.Label(ventana_portada,
    relief="raised",bg="aqua",fg="black", text="¡BIENVENIDOS al Mini-proyecto!", 
    font=("Arial", 20), width=40, height=2, anchor="center")
label_bienvenida.pack(padx=20, pady=20)

# Cargar la imagen de portada
imagen = PhotoImage(file="equipo5.png").subsample(2,2)  # cargar la imagen y dar las dimensiones
label_imagen = tk.Label(ventana_portada, image=imagen)
label_imagen.pack()
# Función para cerrar la ventana de portada y abrir la ventana principal
def abrir_ventana_principal():
    ventana_portada.destroy()



    

# Botón de inicio que aparece en la portada.
# Este botón al hacer clic se cierra.
boton_inicio = tk.Button(ventana_portada, text="Iniciar", bg="#2F4F4F", fg="white", 
padx=10, pady=5, font=("Arial", 12), 
command=abrir_ventana_principal)
boton_inicio.pack(pady=20)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Entrada y Salida de Empleados")
ventana.geometry("600x600")
ventana.config(bg= "#808000")

Label(ventana, text="").pack()  # Separador

etiqueta = tk.Label(ventana, 
    text="Registro: ENTRADA Y SALIDA DE EMPLEADOS",
    relief="raised", bg="aqua", fg="black", font=("Arial", 16),
    width=40, height=2, anchor="center")
etiqueta.pack()

""" Función para actualizar el reloj
def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
   
    #etiqueta_reloj.config(text=  hora_actual)
    ventana.after(1000, actualizar_reloj)"""

# Función para actualizar fecha y hora 
def actualizar_fecha():
    #fecha_hora=datetime.now()
    fecha_actual= time.strftime('%d/%m/%y'),
    etiqueta_fecha.config(text=fecha_actual)
    ventana.after(1000, actualizar_fecha)
    
def actualizar_hora():
    hora_actual= time.strftime('%H:%M:%S')
    etiqueta_hora.config(text=hora_actual)
    ventana.after(1000, actualizar_hora)

# Función para cerrar la ventana de portada y abrir la ventana principal
def abrir_ventana_principal():
    ventana_portada.destroy()


# Función para manejar el registro de entrada/salida
def registrar_entrada_salida(accion):
    nombre_empleado = combo_empleados.get()
    if nombre_empleado:
        mensaje = f"{nombre_empleado} ha registrado su {accion} a las {time.strftime('%H:%M:%S')} del día {time.strftime ("%d/%m/%y")}"
        lista_registro.insert(tk.END, mensaje)
    else:
        mensaje_error.config(text="¡Seleccione un empleado!")

# Función para agregar un nuevo empleado
def agregar_empleado():
    nuevo_empleado = entrada_nuevo_empleado.get()
    if nuevo_empleado:
        empleados.append(nuevo_empleado)
        actualizar_lista_empleados()
        entrada_nuevo_empleado.delete(0, tk.END)

# Función para actualizar la lista de empleados en el combobox
def actualizar_lista_empleados():
    combo_empleados['values'] = empleados

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
    
    def seleccionar_empleado(event):
        seleccion = listbox_empleados.curselection()
        if seleccion:
            seleccionado = listbox_empleados.get(seleccion)
            combo_empleados.set(seleccionado)
        ventana_lista.destroy()
    
    listbox_empleados.bind('<<ListboxSelect>>', seleccionar_empleado)

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
            actualizar_lista_empleados()
            ventana_eliminar.destroy()
    
    boton_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion)
    boton_confirmar.pack(pady=10)



# Menú de la aplicación
menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Reloj
#etiqueta_reloj = tk.Label(ventana, fg="aqua",bg="black", font=('Arial', 14))
#etiqueta_reloj.pack(pady=10)
#actualizar_reloj()

#Fecha
etiqueta_fecha = tk.Label(ventana,  text= "Fecha:", fg="aqua",bg="black", font=('Arial', 14))
etiqueta_fecha.pack(pady=10)
actualizar_fecha()
etiqueta_hora = tk.Label(ventana, text= "Hora:", fg="aqua",bg="black", font=('Arial', 14))
etiqueta_hora.pack(pady=10)

actualizar_hora()

# Lista de empleados (menú desplegable)
label_empleado = tk.Label(ventana, text="Seleccione su nombre:")
label_empleado.pack(pady=5)

empleados = ["Juan Pérez", "María López", "Carlos Sánchez", "Ana García"]
combo_empleados = ttk.Combobox(ventana, values=empleados)
combo_empleados.pack(pady=5)

# Botón para abrir la lista de empleados con scroll
boton_lista_completa = tk.Button(ventana, bg="aqua", text="Ver lista completa", command=abrir_lista_empleados)
boton_lista_completa.pack(pady=5)

# Botones de Entrada y Salida
boton_entrada = tk.Button(ventana,bg="aqua", text="Entrada", command=lambda: registrar_entrada_salida("entrada"))
boton_entrada.pack(pady=5)

boton_salida = tk.Button(ventana, bg="aqua",text="Salida", command=lambda: registrar_entrada_salida("salida"))
boton_salida.pack(pady=5)

# Etiqueta para mensajes de error
mensaje_error = tk.Label(ventana, text="", fg="red")
mensaje_error.pack(pady=5)

# Cuadro de entrada para agregar nuevo empleado
label_nuevo_empleado = tk.Label(ventana, text="Agregar nuevo empleado:")
label_nuevo_empleado.pack(pady=5)
entrada_nuevo_empleado = tk.Entry(ventana)
entrada_nuevo_empleado.pack(pady=5)
boton_agregar_empleado = tk.Button(ventana, bg="aqua", text="Agregar:", command=agregar_empleado)
boton_agregar_empleado.pack(pady=5)

# Botón para eliminar empleado
boton_eliminar_empleado = tk.Button(ventana, bg="aqua",
    text="Eliminar empleado", command=eliminar_empleado)
boton_eliminar_empleado.pack(pady=5)

# Lista de registros (con barra de desplazamiento)
frame_registro = tk.Frame(ventana)
frame_registro.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_registro)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_registro = tk.Listbox(frame_registro,
            yscrollcommand=scrollbar.set)
lista_registro.pack(side=tk.LEFT, fill=tk.BOTH,
        expand=True)

scrollbar.config(command=lista_registro.yview)

# Iniciar el bucle de la aplicación
ventana.mainloop()