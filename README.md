import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
#from tkinter import  filedialog as fd
import time     # from datetime import datetime/ también cirve para fecha
import locale   #cambia idioma 
locale.setlocale(locale.LC_TIME, "es_ES") #locale.setlocale(locale.LC_ALL, 'esp') 


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Entrada y Salida de Empleados")
ventana.geometry("600x600")
ventana.config(background='orange')
ventana.minsize(width=500, height=500)


# Función para actualizar el reloj
def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta_reloj.config(text=hora_actual)
    ventana.after(1000, actualizar_reloj)
    dato_semana = time.strftime('%A %d %B, %Y')  
    etiqueta_semana.config(text = dato_semana)

# Función para manejar el registro de entrada/salida
def registrar_entrada_salida(accion):
    nombre_empleado = listbox_empleados.get() 
    if nombre_empleado:
        mensaje = f"{nombre_empleado} ha registrado su {accion} a las {time.strftime('%H:%M:%S'),time.strftime('%A %d %B, %Y') }" #agrege fecha
        lista_registro.insert(tk.END, mensaje)
        listbox_empleados.delete(0, tk.END)
        
    else:
        mensaje_error.config(text="¡Seleccione un empleado!") #mensaje error no se quita si cometes error
        
#Archivo que guarda el registro.
    with open('registro_asistencia.txt', 'a',  encoding='utf-8') as f:
        f.write(f"{mensaje} \n") #alt+92 = \  
        etiqueta_resultado.config(text=(f"{mensaje}\n"))
    

# Función para agregar un nuevo empleado
def agregar_empleado():
    nuevo_empleado = entrada_nuevo_empleado.get()
    if nuevo_empleado:
        empleados.append(nuevo_empleado)
        actualizar_lista_empleados()
        entrada_nuevo_empleado.delete(0, tk.END)

# Función para actualizar la lista de empleados en el combobox
def actualizar_lista_empleados():
    listbox_empleados ['values']= empleados
    
    
    

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
            listbox_empleados.set(seleccionado)
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


#ventana registro no agregue/ necesita codigo txt
# def mostrar_ventana_secundaria(ventana):
#     ventana_secundaria = Toplevel(ventana)
#     ventana_secundaria.title("Ventana Secundaria")
#     ventana_secundaria.geometry("500x600")
#     etiqueta_resultado=tk.Label(ventana_secundaria, text=f'registro_asistencia.txt')
#     etiqueta_resultado.pack()  
#     boton_cerrar = tk.Button(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy)
#     boton_cerrar.pack(pady=20)


#campo_texto=tk.Entry(ventana)
#Funcion para registrar asistencia// no agregue este
# # def registrar_asistencia():
# #     nombre_empleado=campo_texto.get()
# #     hora_actual= datetime.now().strftime("%Y-%n-%d %H:%M:%S")
# #     with open('registro_asistencia.txt', 'a') as f:
# #         f.write(f"{nombre_empleado}, {hora_actual}\n") #alt+92 = \
# #     etiqueta_resultado.config(text=f"Asistencia registrada para: {nombre_empleado} a las {hora_actual} ")


# Menú de la aplicación
menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Reloj
etiqueta_reloj = tk.Label(ventana, font=('Arial', 16))
etiqueta_reloj.pack()
etiqueta_reloj.place(anchor = 'ne', relx=1, rely=0.05)#n, ne, e, se, s, sw, w, nw, or center
etiqueta_semana=tk.Label(ventana, font=("Arial",16))
etiqueta_semana.pack()
etiqueta_semana.place(anchor = 'ne', relx=1, rely=0.00)

actualizar_reloj()


# Lista de empleados (menú desplegable)
label_empleado = tk.Label(ventana, text="Seleccione su nombre:", font =('Arial', 12), bg = 'orange', fg = 'mediumBlue')
label_empleado.pack()
label_empleado.place(anchor = 'nw', relx=0, rely=0)

#cambie el codigo combo por lista
#empleados = [""]
# combo_empleados = ttk.Combobox(ventana, values=empleados)
# combo_empleados.pack()
# combo_empleados.place(anchor = 'nw', relx=0.20, rely=0.001)

# Crear lista de empleados, no guarda nombres.
empleados =["",]
#"Juan Pérez", "María López", "Carlos Sánchez", "Ana García"
listbox_empleados = ttk.Combobox(ventana, values= empleados, state='readonly')
listbox_empleados.current(0)  # Establecer el valor por defecto
listbox_empleados.pack()
listbox_empleados.place(anchor = 'nw', relx=0.20, rely=0.001)

# Botón para abrir la lista de empleados con scroll
boton_lista_completa = tk.Button(ventana, text="Ver lista completa", font =('Arial', 12), bg = 'blue', fg = 'black', command=abrir_lista_empleados)
boton_lista_completa.pack()
boton_lista_completa.place(anchor = 'nw', relx=0.02, rely=0.05)

# Botones de Entrada y Salida
boton_entrada = tk.Button(ventana, text="Entrada", command=lambda: registrar_entrada_salida("entrada"))
boton_entrada.pack()
boton_entrada.place(anchor = 'nw', relx=0.20, rely=0.05)

boton_salida = tk.Button(ventana, text="Salida", command=lambda: registrar_entrada_salida("salida"))
boton_salida.pack()
boton_salida.place(anchor = 'nw', relx=0.30, rely=0.05)

#Boton de registro no agregue 
# boton= tk.Button(ventana, text="Registro de asistencia", command=lambda:mostrar_ventana_secundaria(ventana))
# boton.pack()

# Etiqueta para mensajes de error
mensaje_error = tk.Label(ventana, text="", fg="yellow", bg= 'black', font =('Arial', 20))
mensaje_error.pack()
mensaje_error.place(anchor = 'nw', relx=0, rely=0.10)



#Etiqueta de registro 
etiqueta_resultado=tk.Label(ventana, text="", bg= 'orange')
#etiqueta_resultado.pack() lo borre porque me mostrava en ventana
# resultado=tk.Label()
# resultado.pack()

# Cuadro de entrada para agregar nuevo empleado
label_nuevo_empleado = tk.Label(ventana, text="Agregar nuevo empleado:", font =('Arial', 12), bg = 'orange', fg = 'mediumBlue')
label_nuevo_empleado.pack()
label_nuevo_empleado.place(anchor = 'nw', relx=0.00, rely=0.20)

entrada_nuevo_empleado = tk.Entry(ventana)
entrada_nuevo_empleado.pack()
entrada_nuevo_empleado.place(anchor = 'nw', relx=0.20, rely=0.20)

boton_agregar_empleado = tk.Button(ventana, text="Agregar", command=agregar_empleado)
boton_agregar_empleado.pack()
boton_agregar_empleado.place(anchor = 'nw', relx=0.20, rely=0.25)

# Botón para eliminar empleado
boton_eliminar_empleado = tk.Button(ventana, text="Eliminar empleado", command=eliminar_empleado)
boton_eliminar_empleado.pack()
boton_eliminar_empleado.place(anchor = 'nw', relx=0.30, rely=0.25)

# Lista de registros (con barra de desplazamiento)
frame_registro = tk.Frame(ventana)
frame_registro.pack(fill=tk.X, expand=True)

scrollbar = tk.Scrollbar(frame_registro)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

lista_registro = tk.Listbox(frame_registro, yscrollcommand=scrollbar.set)
lista_registro.pack(fill=tk.X, expand=True)

scrollbar.config(command=lista_registro.yview)



# Iniciar el bucle de la aplicación
ventana.mainloop()




# with open('mi_archivo.txt', 'w', encoding='utf-8') as archivo:
# archivo.write(texto)
#el parametro encoding='utf-8' debería permitirte guardar los caracteres especiales en el archivo que se abre para escritura
