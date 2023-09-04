import asyncio
import threading
import sqlite3

import tkinter as tk

root = tk.Tk()
root.title("DALM1TCPChat")

# Crée l'entrée
entry = tk.Entry(root)
entry.pack()

def send_message(message):
  asyncio.run(send_message(message))


# Crée une base de données pour stocker les informations sur les clients et les discussions
conn = sqlite3.connect("chat.db")
cur = conn.cursor()

# Commente la ligne ci-dessous si la table discussions existe déjà
# cur.execute("CREATE TABLE discussions (id INTEGER PRIMARY KEY, name TEXT, participants TEXT)")

# Ajoute le client actuel à la table des clients
cur.execute("INSERT INTO clients (name, ip, port) VALUES ('[Votre nom]', '127.0.0.1', 8080)")
conn.commit()


# Traite les messages du serveur
async def handle_message(message):
  # Affiche le message dans la zone de texte
  text.insert(tk.END, message + "\n")


# Crée un thread pour traiter les messages du serveur
thread = threading.Thread(target=handle_message)
thread.start()

# Exécution de la boucle d'événements dans le thread principal
asyncio.run(root.mainloop())

def on_enter(event):
  message = entry.get()
  send_message(message=message)

button = tk.Button(root, text="Envoyer", command=on_enter)
button.pack()

entry.bind("<Return>", on_enter)
