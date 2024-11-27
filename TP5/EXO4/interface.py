import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x300")
root.title('interface_USER')


LABEL1 = ctk.CTkLabel(root, text='Ajouter un utilisateur', font=('Times new roman', 22))
LABEL1.place(x=200, y=10)



















entry_affiche = ctk.CTkTextbox(root, border_width=2, corner_radius=8, width=500, height=400)
entry_affiche.place(x=700, y=50)

BOUTON_QUITTER = ctk.CTkButton(root, text="Quitter", corner_radius=17, width=60, height=30, command=root.quit)
BOUTON_QUITTER.place(x=900, y=500)



root.mainloop()