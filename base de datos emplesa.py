import sqlite3

import tkinter as tk



conexion=sqlite3.connect("/home/programador10/Desktop/archivis/base de datos en grupo.db")
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

######################################################################################################################################3
def ver_lista():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM empleados")

    for u in cursor.fetchall():
        lista.insert(tk.END, u)
        print("222")

def modificar_nombre():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE empleados SET nombre_y_apellido = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()


def modificar_asistencia():
    
    t1=entrada1.get()
    t2=entrada5.get()
    cursor.execute("UPDATE empleados SET asistencias = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()

def anios_trabajados():
    
    t1=entrada1.get()
    t2=entrada5.get()
    cursor.execute("UPDATE empleados SET anios_trabajados = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    
def borar():
    
    t1=entrada1.get()
    cursor.execute("DELETE FROM empleados WHERE id=?",(t1,))
    conexion.commit()
    ver_lista()
    
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

busca=tk.Label(ventana, text="")
busca.pack()

tk.Button(ventana,text="agregar producto",command=agragar_data).pack()
tk.Button(ventana,text="modificar nombre de emplesa",command=md_nombre_sucursales).pack()
tk.Button(ventana,text="modificar presio de emplesa",command=md_direccion_sucursales).pack()
tk.Button(ventana,text="buscador",command=lista_empleados).pack()


lista=tk.Listbox(ventana)
lista.pack()

lista2=tk.Listbox(ventana)
lista2.pack()

ver_lista()

ventana.mainloop()