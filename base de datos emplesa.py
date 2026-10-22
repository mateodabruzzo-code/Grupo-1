import sqlite3

import tkinter as tk



conexion=sqlite3.connect("base de datos en grupo.db")
cursor=conexion.cursor()


cursor.execute(""" 
         
CREATE TABLE IF NOT EXISTS sucursales (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre_sucursal TEXT,
dureccion INTEGER


)            
""")   
conexion.commit()

cursor.execute(""" 
        
CREATE TABLE IF NOT EXISTS empleados (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre_y_apellido TEXT,
anios_contratado INTEGER,
anios_trabajados INTEGER,
asistencias INTEGER,
dni INTEGER,
id_sucursal INTEGER


)            
""")   
conexion.commit()


def ver_lista():
    
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM sucursales")

    for u in cursor.fetchall():
        lista.insert(tk.END, u)
        print("222")

def agragar_data():
    t1=entrada2.get()
    t2=entrada3.get()

    cursor.execute(
                
    "INSERT INTO sucursales (nombre_sucursal,dureccion) VALUES (?,?)",(t1,t2)
                
    )
    conexion.commit()   

    ver_lista() 
    

def md_nombre_sucursales():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE sucursales SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()

def md_direccion_sucursales():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE sucursales SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    



def buscar():
    
    et=int(entrada1.get())

    print("holaaaaa1")

    cursor.execute("SELECT * FROM sucursales WHERE id = ?", (et,))
    print("holaaaaa2")

    idbusca=cursor.fetchall()
    for i in idbusca:
        print("holaaaaa")
        print("paa")
        if et in i:
            busca.config(text=i) 
            print("sssssssss")
        else:
            busca.config(text="contacto no encontrado")
            print("nnnnnnnnnn")
            
def lista_empleados():
    et=int(entrada1.get())
    cursor.execute("SELECT * FROM empleados WHERE id_sucursal = ?", (et,))

    idbusca=cursor.fetchall()
    for i in idbusca:
        print("holaaaaa")
        print("paa")
        if et in i:
            lista2.insert(tk.END, et)
            print("222")
        else:
            busca.config(text="contacto no encontrado")
            print("nnnnnnnnnn")

######################################################################################################################################
#empleados
def ver_lista():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM empleados")
    for u in cursor.fetchall():
        lista.insert(tk.END, u)
        
def comprobar(empleado,entry_,orden):
    variable=entry_.get()
    if variable=="":
        print(empleado[orden])
        return empleado[orden]
    else:
        print(variable)
        return variable
    
def new_empleado():
    nom_ape=entry_nom_ape.get()
    anio_inicio=entry_anio_inicio.get()
    anios_trabajados=entry_anios_trabajados.get()
    asist=entry_asistencias.get()
    dni=entry_dni.get()
    cursor.execute("INSERT INTO empleados (nombre_y_apellido,anios_contratado,anios_trabajados,asistencias,dni) VALUES (?,?,?,?,?)",(nom_ape,anio_inicio,anios_trabajados,asist,dni))
    conexion.commit()
    ver_lista()
    limpiar_entry_empleados()
    
def editar_empleado():
    p_id=entry_id.get()
    cursor.execute("SELECT * FROM empleados")
    empleados=cursor.fetchall()
    for empleado in empleados:
        if p_id==empleado[0]:
            nom_ape=comprobar(empleado,entry_nom_ape,1)
            anios_trabajados=comprobar(empleado,anios_trabajados,3)
            asist=comprobar(empleado,entry_asistencias,4)
            cursor.execute("UPDATE empleados SET nombre_y_apellido = ?, anios_trabajados = ?, asistencias = ? WHERE id = ?",(nom_ape,anios_trabajados,p_id,asist))
            conexion.commit()
            ver_lista()
            limpiar_entry_empleados()

def eliminar_empleado():
    p_id=entry_id.get()
    cursor.execute("DELETE FROM empleados WHERE id = ?",(p_id,))
    conexion.commit()
    ver_lista()
    limpiar_entry_empleados()

def limpiar_entry_empleados():
    entry_id.delete(0,tk.END)
    entry_nom_ape.delete(0,tk.END)
    entry_anio_inicio.delete(0,tk.END)
    entry_anios_trabajados.delete(0,tk.END)
    entry_asistencias.delete(0,tk.END)
    entry_dni.delete(0,tk.END)
    
def buscar():    
    et=int(entrada1.get())

    print("holaaaaa1")

    cursor.execute("SELECT * FROM empleados WHERE id = ?", (et,))
    print("holaaaaa2")

    idbusca=cursor.fetchall()
    for i in idbusca:
        print("holaaaaa")
        print("paa")
        if et in i:
            busca.config(text=i) 
            print("sssssssss")
        else:
            busca.config(text="contacto no encontrado")
            print("nnnnnnnnnn")

#####################################################################################################################################

ventana = tk.Tk()
ventana.title("Prueba Multiprocessing")
ventana.geometry("400x650")

resultado=tk.Label(ventana, text="ID")
resultado.pack()
entrada1=tk.Entry(ventana)
entrada1.pack()
resultado=tk.Label(ventana, text="nombre emplesa")
resultado.pack()
entrada2=tk.Entry(ventana)
entrada2.pack()
resultado=tk.Label(ventana, text="direccion")
resultado.pack()
entrada3=tk.Entry(ventana)
entrada3.pack()


tk.Button(ventana,text="agregar producto",command=agragar_data).pack()
tk.Button(ventana,text="modificar nombre de emplesa",command=md_nombre_sucursales).pack()
tk.Button(ventana,text="modificar presio de emplesa",command=md_direccion_sucursales).pack()
tk.Button(ventana,text="buscador",command=lista_empleados).pack()


lista=tk.Listbox(ventana)
lista.pack()

lista2=tk.Listbox(ventana)
lista2.pack()

ver_lista()

###############################################################
#NEW VENTANA DE EMPLEADOS AQUI

label_id=tk.Label(ventana, text="ID")
label_id.pack()
entry_id=tk.Entry(ventana)
entry_id.pack()

label_nom_ape=tk.Label(ventana, text="nombre_apellido")
label_nom_ape.pack()
entry_nom_ape=tk.Entry(ventana)
entry_nom_ape.pack()

label_anio_inicio=tk.Label(ventana, text="anio de inicio")
label_anio_inicio.pack()
entry_anio_inicio=tk.Entry(ventana)
entry_anio_inicio.pack()

label_anios_trabajados=tk.Label(ventana, text="anios trabajados")
label_anios_trabajados
entry_anios_trabajados=tk.Entry(ventana)
entry_anios_trabajados.pack()

label_asistencias=tk.Label(ventana, text="asistencias")
label_asistencias.pack()
entry_asistencias=tk.Entry(ventana)
entry_asistencias.pack()

label_dni=tk.Label(ventana, text="asistencias")
label_dni.pack()
entry_dni=tk.Entry(ventana)
entry_dni.pack()

busca=tk.Label(ventana, text="")
busca.pack()

ventana.mainloop()