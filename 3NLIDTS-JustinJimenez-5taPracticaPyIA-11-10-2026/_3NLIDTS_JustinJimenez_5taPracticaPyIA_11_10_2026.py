import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

def EnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        messagebox.showerror("Error Edad", "Valor de edad equivocado")
        return False

def DecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def TelefonoValido(valor):
    return valor.isdigit() and len(valor) == 10

def TextoValido(valor):
    return bool(re.match("^[a-zA-Z\\s]+$", valor))

def borrar():
    # Mejora 1: Cuadro modal de confirmación preventiva
    confirmacion = messagebox.askyesno(
        "Confirmar limpieza",
        "¿Está seguro de que desea limpiar todos los campos del formulario?"
    )
    if confirmacion:
        tbNombre.delete(0, tk.END)
        tbApellidos.delete(0, tk.END)
        tbEdad.delete(0, tk.END)
        tbTelefono.delete(0, tk.END)
        tbEstatura.delete(0, tk.END)
        rbSeleccionGenero.set(0)
        tbNombre.focus()

def guardar():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    tel = tbTelefono.get()
    estatura = tbEstatura.get()
    genero = ""

    if rbSeleccionGenero.get() == 1:
        genero = "Masculino"
    elif rbSeleccionGenero.get() == 2:
        genero = "Femenino"
    elif rbSeleccionGenero.get() == 3:
        genero = "No Definido"

    if (EnteroValido(edad) and DecimalValido(estatura) and
        TelefonoValido(tel) and TextoValido(nombres) and
        TextoValido(apellidos)):
        
        # Mejora 2: Registro con marca temporal de fecha y hora
        fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        datos = ("Fecha y Hora: " + fecha_registro + "\n" +
                 "Nombre: " + nombres + "\n" +
                 "Apellidos: " + apellidos + "\n" +
                 "Edad: " + edad + "\n" +
                 "Telefono: " + tel + "\n" +
                 "Estatura: " + estatura + "\n" +
                 "Genero: " + genero)
        
        ruta = r"C:\Users\omnib\OneDrive\Documents\Datos3D_13Feb26.txt"
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n\n")
            
        messagebox.showinfo("Informacion", "Datos guardados correctamente \n\n" + datos)
    else:
        messagebox.showerror("Error", "Algunos de los campos tienen Formato equivocado")

ventana = tk.Tk()
ventana.configure(bg="pink")
ventana.geometry("350x550")
ventana.title("Actividad 04 - Formulario de Registro Vr. 001")

rbSeleccionGenero = tk.IntVar()

tk.Label(ventana, text="Nombre:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack()

tk.Label(ventana, text="Apellidos:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbApellidos = tk.Entry(ventana, width=35, justify="center")
tbApellidos.pack()

tk.Label(ventana, text="Edad:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbEdad = tk.Entry(ventana, width=10, justify="center")
tbEdad.pack()

tk.Label(ventana, text="Estatura:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbEstatura = tk.Entry(ventana, width=15, justify="center")
tbEstatura.pack()

tk.Label(ventana, text="Telefono:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack()

gb = tk.LabelFrame(ventana, text="Selecione un Genero", padx=10, pady=8)
gb.pack(padx=10, pady=8)
rbMasculino = tk.Radiobutton(gb, text="Masculino", value=1, variable=rbSeleccionGenero)
rbMasculino.grid(column=1, row=1)
rbFemenino = tk.Radiobutton(gb, text="Femenino", value=2, variable=rbSeleccionGenero)
rbFemenino.grid(column=2, row=1)
rbNoDefinido = tk.Radiobutton(gb, text="No Definido", value=3, variable=rbSeleccionGenero)
rbNoDefinido.grid(column=3, row=1)

gb2 = tk.LabelFrame(ventana, text="")
gb2.pack(padx=10, pady=8)
btnGuardar = tk.Button(gb2, text="Guardar", width=10, padx=10, pady=8, command=guardar)
btnGuardar.grid(column=1, row=1)
btnBorrar = tk.Button(gb2, text="Borrar", width=10, padx=10, pady=8, command=borrar)
btnBorrar.grid(column=2, row=1)

ventana.mainloop()