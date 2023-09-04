import asyncio
import threading
import sqlite3

import tkinter as tk


async def send_message(message):
  # Envoie le message au serveur
  connection = await asyncio.open_connection("localhost", 8080)
  connection.sendall(message.encode())

  # Attend la réponse du serveur
  data = await connection.recv(b"1024")

  # Affiche la réponse du serveur
  print(data.decode())


def main():
  # Crée une base de données pour stocker les informations sur les clients et les discussions
  conn = sqlite3.connect("chat.db")
  cur = conn.cursor()

  # Commente la ligne ci-dessous si la table discussions existe déjà
  # cur.execute("CREATE TABLE discussions (id INTEGER PRIMARY KEY, name TEXT, participants TEXT)")

  # Ajoute le client actuel à la table des clients
  cur.execute("INSERT INTO clients (name, ip, port) VALUES ('[Votre nom]', '127.0.0.1', 8080)")
  conn.commit()


  # Crée une fenêtre Tkinter
  root = tk.Tk()

  # Crée l'entrée
  entry = tk.Entry(root)
  entry.pack()

  # Crée un bouton pour envoyer le message
  button = tk.Button(root, text="Envoyer", command=lambda: send_message(message=entry.get()))
  button.pack()

  # Crée une boucle d'événements pour traiter les messages du serveur
  asyncio.run(root.mainloop())


if __name__ == "__main__":
  main()
