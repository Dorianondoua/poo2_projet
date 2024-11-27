import customtkinter as ctk
from PIL import Image

def destroy():
    root.destroy()



def valider():
    prenom = ENTRY1.get()
    nom = ENTRY2.get()
    ville = ENTRY3.get()
    ENTRY4.delete(0, ctk.END)  # Effacer le contenu précédent
    ENTRY4.insert(0, f"{prenom}/{nom}/{ville}")  # Afficher les informations

def reinitialiser():
    ENTRY1.delete(0, ctk.END)
    ENTRY2.delete(0, ctk.END)
    ENTRY3.delete(0, ctk.END)
    ENTRY4.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("400x300")
root.title("app tk")

LABEL1 = ctk.CTkLabel(root, text='Entrez votre prénom :', font=('Times new roman', 17))
LABEL1.place(x=100, y=60)

ENTRY1 = ctk.CTkEntry(root, width=250, height=25)
ENTRY1.place(x=280, y=60)

LABEL2 = ctk.CTkLabel(root, text='Entrez votre nom :', font=('Times new roman', 17))
LABEL2.place(x=100, y=130)

ENTRY2 = ctk.CTkEntry(root, width=250, height=25)
ENTRY2.place(x=280, y=130)

LABEL3 = ctk.CTkLabel(root, text='Entrez votre ville :', font=('Times new roman', 17))
LABEL3.place(x=100, y=200)

ENTRY3 = ctk.CTkEntry(root, width=250, height=25)
ENTRY3.place(x=280, y=200)

ENTRY4 = ctk.CTkEntry(root, width=300, height=45)
ENTRY4.place(x=80, y=270)

BOUTON_VALIDER = ctk.CTkButton(root, text="Valider", corner_radius=17, width=60, height=30, command=valider)
BOUTON_VALIDER.place(x=120, y=350)

BOUTON_REINIT = ctk.CTkButton(root, text="Réinitialiser", corner_radius=17, width=60, height=30, command=reinitialiser)
BOUTON_REINIT.place(x=250, y=350)

BOUTON_QUITTER = ctk.CTkButton(root,text="Quitter", corner_radius=17, width=60, height=30, command=destroy)
BOUTON_QUITTER.place(x=700, y=430)

frame = ctk.CTkFrame(root, width=500, height=350)
frame.place(x=570, y=50)

# Charger une image avec Pillow et CTkImage
image = ctk.CTkImage(Image.open("IMG_E6430.jpg"), size=(600, 350))

# Ajouter l'image à un CTkLabel
label_image = ctk.CTkLabel(frame, image=image, text="")
label_image.pack()

root.mainloop()