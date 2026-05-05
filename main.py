import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import datetime

from gestor_usuarios import GestorUsuarios
from reserva import Reserva
from servicios import ReservaSala

# -------------------------
# Función guardar
# -------------------------


def guardar_log(texto):
    with open("bitacora.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {texto}\n")

db = GestorUsuarios()


# -------------------------
# FUNCIÓN: REGISTRAR CLIENTE
# -------------------------

def registrar_cliente():
    try:
        n = e_n.get().strip()
        a = e_a.get().strip()
        d = e_d.get().strip()
        t = e_t.get().strip()
        dir = e_dir.get().strip()

        # VALIDACIÓN DE NOMBRES 
        if not n:
            raise ValueError("El nombre no puede estar vacío.")
        if not all(p.isalpha() for p in n.split()):
            raise ValueError("El nombre solo debe contener letras.")

        # VALIDACIÓN DE APELLIDOS
        if not a:
            raise ValueError("El apellido no puede estar vacío.")

        # VALIDACIÓN DE DOCUMENTO
        if not d.isdigit():
            raise ValueError("El documento debe contener solo números.")
        if len(d) > 10:
            raise ValueError("Documento numérico de máximo 10 dígitos.")

        # VALIDACIÓN DE TELÉFONO
        if not t.isdigit():
            raise ValueError("El teléfono debe contener solo números.")
        if len(t) != 10:
            raise ValueError("El teléfono debe tener exactamente 10 dígitos.")

        # REGISTRO REAL
        db.registrar(n, a, d, t, dir)
        messagebox.showinfo("Éxito", "Cliente registrado correctamente")

        # Limpiar campos
        e_n.delete(0, tk.END)
        e_a.delete(0, tk.END)
        e_d.delete(0, tk.END)
        e_t.delete(0, tk.END)
        e_dir.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------
# FUNCIÓN: VER CLIENTES
# -------------------------
def ver_clientes():
    salida.delete("1.0", tk.END)
    for c in db._lista:
        salida.insert(
            tk.END,
            f"{c.documento_identidad} - {c.nombres} {c.apellidos} - Tel: {c.telefono}\n"
        )

# -------------------------
# FUNCIÓN: SIMULACIÓN
# -------------------------
def simulacion():
    salida.delete("1.0", tk.END)
    guardar_log("Inicio de simulación de 10 operaciones.")

    docs = ["1010", "2020", "0000", "3030", "4040", "1234", "1010", "5555", "6666", "7777"]
    sala = ReservaSala("S1", "Sala de Espera Central", 40000)

    for i, d in enumerate(docs, 1):
        try:
            salida.insert(tk.END, f"Prueba {i}: Cédula {d}\n")
            persona = db.buscar(d)

            if not persona:
                salida.insert(tk.END, "Cliente no existe. Creando uno...\n")
                persona = db.registrar("Auto", "Generado", d, "3000000000", "N/A")

            res = Reserva(persona, sala, 1)
            salida.insert(tk.END, res.procesar() + "\n\n")

        except Exception as e:
            guardar_log(f"Fallo en prueba {i}: {e}")
            salida.insert(tk.END, f"Error: {e} (Registrado en bitácora)\n\n")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
root = tk.Tk()
root.title("Sistema de Reservas")
root.geometry("650x600")

# -------------------------
# CAMPOS DE REGISTRO
# -----------------------

tk.Label(root, text="Nombres:").pack()
e_n = tk.Entry(root, width=40)
e_n.pack()

tk.Label(root, text="Apellidos:").pack()
e_a = tk.Entry(root, width=40)
e_a.pack()

tk.Label(root, text="Documento:").pack()
e_d = tk.Entry(root, width=40)
e_d.pack()

tk.Label(root, text="Teléfono:").pack()
e_t = tk.Entry(root, width=40)
e_t.pack()

tk.Label(root, text="Dirección:").pack()
e_dir = tk.Entry(root, width=40)
e_dir.pack()

# -------------------------
# BOTONES
# -------------------------
tk.Button(root, text="Registrar Cliente", width=25, command=registrar_cliente).pack(pady=10)
tk.Button(root, text="Ver Clientes", width=25, command=ver_clientes).pack(pady=10)
tk.Button(root, text="Simulación (10 operaciones)", width=25, command=simulacion).pack(pady=10)
tk.Button(root, text="Salir", width=25, command=root.destroy).pack(pady=10)

# -------------------------
# CUADRO DE SALIDA
# -------------------------
salida = ScrolledText(root, wrap=tk.WORD, width=70, height=15)
salida.pack(pady=10)

root.mainloop()
