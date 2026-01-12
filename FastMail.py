import pywhatkit as kit
import tkinter as tk
from tkinter import messagebox


def enviar_correo_gui():
    # Obtenemos los datos de los campos de entrada
    remitente = entry_mail.get()
    password = entry_pass.get()
    asunto = entry_subject.get()
    # Lee desde la primera línea hasta el final
    mensaje = txt_msg.get("1.0", tk.END)
    destinatario = entry_dest.get()
    kit.send_mail(remitente, password, asunto, mensaje, destinatario)

    # Validación básica
    if not remitente or not password or not destinatario:
        messagebox.showwarning("Campos vacíos",
                               "Por favor, completa los "
                               "campos obligatorios.")
        return

    try:
        kit.send_mail(remitente, password, asunto, mensaje, destinatario)
        messagebox.showinfo("Éxito", "El correo se ha enviado correctamente.")
        # Limpiamos el mensaje después de enviar
        txt_msg.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo:\n{e}")


def mostrar_ayuda():
    ayuda = """si no tienes una contraseña de aplicación:\n
            Ve a:
            https://support.google.com/accounts/answer/185833?hl=es\n
            y crea una contraseña de aplicación"""
    messagebox.showinfo("Ayuda - Contraseña de Aplicación", ayuda)


# --- Configuración de la Ventana Principal ---
root = tk.Tk()
root.title("FastMail")
root.geometry("800x600")
root.config(padx=20, pady=20)

# --- Etiquetas y Campos de Entrada ---
tk.Label(root, text="* Tu Correo (Gmail):",
         font=('Arial', 10, 'bold')).pack(anchor="w")
entry_mail = tk.Entry(root, width=50)
entry_mail.pack(pady=5)

tk.Label(root, text="* Contraseña de Aplicación:",
         font=('Arial', 10, 'bold')).pack(anchor="w")
# Oculta la contraseña
entry_pass = tk.Entry(root, width=50, show="*")
entry_pass.pack(pady=5)

# --- Botón de Ayuda ---
btn_ayuda = tk.Button(root, text="?", command=mostrar_ayuda,
                      bg="blue", fg="white")
btn_ayuda.pack(pady=5)

tk.Label(root, text="* Destinatario:",
         font=('Arial', 10, 'bold')).pack(anchor="w")
entry_dest = tk.Entry(root, width=50)
entry_dest.pack(pady=5)

tk.Label(root, text="* Asunto:",
         font=('Arial', 10, 'bold')).pack(anchor="w")
entry_subject = tk.Entry(root, width=50)
entry_subject.pack(pady=5)
# Cuadro de texto más grande
tk.Label(root, text="* Mensaje:",
         font=('Arial', 10, 'bold')).pack(anchor="w")
txt_msg = tk.Text(root, width=50, height=10)
txt_msg.pack(pady=5)

# --- Botón de Envío ---
btn_enviar = tk.Button(root, text="Enviar Correo",
                       command=enviar_correo_gui,
                       bg="#4CAF50", fg="white",
                       font=('Arial', 10, 'bold'), pady=10)
btn_enviar.pack(fill="x", pady=20)

# Iniciar la aplicación
root.mainloop()
