import tkinter as tk

root = tk.Tk()
root.title("TCP Chat")
root.configure(background="white")

# Crée une zone de texte pour afficher les messages
text = tk.Text(root)
text.pack()

# Crée une entrée pour saisir les messages
entry = tk.Entry(root)
entry.pack()

# Définit la fonction appelée lorsque l'utilisateur appuie sur la touche entrée
def send_message():
  # Récupère le message dans l'entrée
  message = entry.get()

  # Envoie le message au serveur
  socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connect_to_server(socket, "localhost", 8080)

  # Efface le message de l'entrée
  entry.delete(0, tk.END)


button = tk.Button(root, text="Envoyer", command=send_message)
button.pack()

# Crée une base de données pour stocker les informations sur les clients et les discussions
conn = sqlite3.connect("chat.db")
cur = conn.cursor()

# Crée une table pour stocker les discussions
cur.execute("CREATE TABLE discussions (id INTEGER PRIMARY KEY, name TEXT, participants TEXT)")

# Ajoute le client actuel à la table des clients
cur.execute("INSERT INTO clients (name, ip, port) VALUES ('[Votre nom]', '127.0.0.1', 8080)")
conn.commit()

# Traite les messages du serveur
def handle_message(message):
  # Affiche le message dans la zone de texte
  text.insert(tk.END, message + "\n")

# Crée un thread pour traiter les messages du serveur
thread = threading.Thread(target=handle_message)
thread.start()

root.mainloop()
