import customtkinter  as ctk
import sqlite3

# Création de la base de données
conn = sqlite3.connect('notes.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS notes (note TEXT, balise TEXT)''')
conn.commit()

root = ctk.CTk()
root.geometry('400x500')
root.title('Appli Note')

# Fonction pour ajouter une note
def ajouter_note():
    note = ENTRY2.get()
    balise = ENTRY3.get()
    if note and balise:
        c.execute("INSERT INTO notes (note, balise) VALUES (?, ?)", (note, balise))
        conn.commit()
        ENTRY2.delete(0, 'end')
        ENTRY3.delete(0, 'end')
        print("Note ajoutée avec succès.")
    else:
        print("Veuillez entrer une note et une balise.")

# Fonction pour réinitialiser les champs
def reinitialiser_champs():
    ENTRY2.delete(0, 'end')
    ENTRY3.delete(0, 'end')
    ENTRY4.delete(0, 'end')


    # Fonction pour afficher les notes

# Fonction pour afficher les notes
def afficher_notes():
    c.execute("SELECT rowid, * FROM notes")  # Récupérer l'ID de la note
    notes = c.fetchall()
    entry_affiche.delete('1.0', 'end')  # Effacer le champ avant d'afficher les nouvelles notes
    for note in notes:
        entry_affiche.insert('end', f"ID: {note[0]}, Note: {note[1]}, Balise: {note[2]}\n")  # Afficher avec ID

# Fonction pour rechercher une note
def rechercher_note():
    terme = ENTRY4.get()
    c.execute("SELECT * FROM notes WHERE note LIKE ?", ('%' + terme + '%',))
    notes = c.fetchall()
    entry_affiche.delete('1.0', 'end')  # Effacer le champ avant d'afficher les résultats
    for note in notes:
        entry_affiche.insert('end', f"Note: {note[0]}, Balise: {note[1]}\n")  # Afficher les résultats dans entry_affiche

# Interface utilisateur
entry_affiche = ctk.CTkTextbox(root, border_width=2, corner_radius=8, width=500, height=400)
entry_affiche.place(x=700, y=50)

LABEL1 = ctk.CTkLabel(root, text='Ajouter une Note', font=('Times new roman', 22))
LABEL1.place(x=200, y=10)

LABEL2 = ctk.CTkLabel(root, text='Entrez la note :', font=('Times new roman', 17))
LABEL2.place(x=200, y=60)

ENTRY2 = ctk.CTkEntry(root, width=350, height=140)
ENTRY2.place(x=340, y=60)

LABEL3 = ctk.CTkLabel(root, text="Entrez la balise :", font=('Times new roman', 17))
LABEL3.place(x=200, y=210)

ENTRY3 = ctk.CTkEntry(root, width=230, height=20)
ENTRY3.place(x=350, y=210)

BOUTON_AJOUTER = ctk.CTkButton(root, text='Ajouter', corner_radius=16, width=40, height=24, command=ajouter_note)
BOUTON_AJOUTER.place(x=420, y=250)

BOUTON_REINIT = ctk.CTkButton(root, text='Réinitialiser', fg_color='red', corner_radius=16, width=40, height=24, command=reinitialiser_champs)
BOUTON_REINIT.place(x=520, y=250)

LABEL4 = ctk.CTkLabel(root, text='Afficher Notes :', font=('Times new roman', 22))
LABEL4.place(x=200, y=290)

BOUTON_AFFICHER = ctk.CTkButton(root, text="Afficher", corner_radius=17, width=60, height=30, command=afficher_notes)
BOUTON_AFFICHER.place(x=340, y=290)

LABEL5 = ctk.CTkLabel(root, text='Rechercher Note', font=('Times new roman', 22))
LABEL5.place(x=200, y=340)

LABEL6 = ctk.CTkLabel(root, text="Entrez le terme :", font=('Times new roman', 17))
LABEL6.place(x=200, y=380)

ENTRY4 = ctk.CTkEntry(root, width=230, height=20)
ENTRY4.place(x=340, y=380)

BOUTON_RECHERCHER = ctk.CTkButton(root, text="Rechercher", corner_radius=17, width=60, height=30, command=rechercher_note)
BOUTON_RECHERCHER.place(x=340, y=420)

BOUTON_QUITTER = ctk.CTkButton(root, text="Quitter", corner_radius=17, width=60, height=30, command=root.quit)
BOUTON_QUITTER.place(x=900, y=500)

root.mainloop()