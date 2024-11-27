import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x300")
root.title("TODO_List")

taches = []  # Liste pour stocker les tâches et leurs états

def ajouter_tache():
    tache = entry.get()
    if tache:
        var = ctk.BooleanVar()  # Variable pour la case à cocher
        taches.append((tache, var))  # Ajoute la tâche et sa variable
        afficher_taches()  # Met à jour l'affichage
        entry.delete(0, ctk.END)

def afficher_taches():
    for widget in frame.winfo_children():
        widget.destroy()  # Efface les widgets précédents
    for tache, var in taches:
        checkbox = ctk.CTkCheckBox(frame, text=tache, variable=var)
        checkbox.pack(anchor='w')  # Ajoute la case à cocher au frame

def supprimer_tache():
    global taches
    taches = [tache for tache in taches if not tache[1].get()]  # Supprime les tâches cochées
    afficher_taches()  # Met à jour l'affichage

def marquer_complet():
    global taches
    for i, (tache, var) in enumerate(taches):
        if var.get():  # Si la case est cochée
            taches[i] = (f"{tache} (complet)", var)  # Marque la tâche comme complète
    afficher_taches()  # Met à jour l'affichage

entry = ctk.CTkEntry(root)
entry.place(x=40, y=50)

frame = ctk.CTkFrame(root, border_width=2, width=300, height=200)
frame.place(x=40, y=100)

bouton_ajouter = ctk.CTkButton(root, text="Ajouter", width=40, height=40, command=ajouter_tache, corner_radius=32)
bouton_ajouter.place(x=70, y=320)

bouton_supprimer = ctk.CTkButton(root, text="Supprimer", command=supprimer_tache, corner_radius=32)
bouton_supprimer.place(x=250, y=50)

bouton_complet = ctk.CTkButton(root, text="Marquer complet", width=30, height=40, command=marquer_complet, corner_radius=32)
bouton_complet.place(x=200, y=320)

root.mainloop()