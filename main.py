import keyboard
import tkinter as tk
from tkinter import messagebox
import time

last_key_press_time = 0.0
idle_time_threshold = 1.0  # Ajustez la période d'inactivité selon vos besoins
pressed_keys = []

def on_key_press(event):
    global last_key_press_time

    current_time = time.time()

    if current_time - last_key_press_time > idle_time_threshold:
        pressed_keys.clear()

    pressed_keys.append(event.name)
    last_key_press_time = current_time

    print("+".join(pressed_keys))
    
def print_keys():
    if pressed_keys:
        print("+".join(pressed_keys))
        pressed_keys.clear()

keyboard.on_press(on_key_press)

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    # Vérifier les informations d'identification génériques
    if username == "utilisateur" and password == "motdepasse":
        messagebox.showinfo("Connexion réussie", "Connexion réussie !")
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")

# Créer une fenêtre
root = tk.Tk()
root.title("Identification générique")

# Créer des widgets pour l'interface utilisateur
label_username = tk.Label(root, text="Nom d'utilisateur:")
entry_username = tk.Entry(root)
label_password = tk.Label(root, text="Mot de passe:")
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Se connecter", command=check_credentials)

# Positionner les widgets dans la fenêtre en utilisant la géométrie de la grille (grid layout)
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username.grid(row=0, column=1, padx=5, pady=5)
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password.grid(row=1, column=1, padx=5, pady=5)
button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

try:
    # Démarrer la boucle principale de l'application
    root.mainloop()
except KeyboardInterrupt:
    print("\nProgramme terminé.")
finally:
    # Libérer les ressources de la bibliothèque keyboard
    keyboard.unhook_all()
