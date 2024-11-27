import tkinter as tk

window = tk.Tk()
window.title("Ma calculatrice")

# Zone d'affichage
button_value = tk.StringVar()
cal_screen = tk.Entry(window, textvariable=button_value, font="Arial 18", justify="right")
cal_screen.grid(row=0, column=0, columnspan=4, ipadx=6, ipady=6)

# Déclaration des buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "+",
    "1", "2", "3", "-",
    "0", ".", "=", "*",
]

def on_click(event):
    global button_value
    text = event.widget.cget("text")
    if text == "=":
        try:
            button_value.set(eval(button_value.get()))
        except Exception as e:
            button_value.set("Erreur d'opération")
    else:
        button_value.set(button_value.get() + text)

row_value = 1
col_value = 0

for button in buttons:
    btn = tk.Button(window, text=button, font="Arial 14", padx=10, pady=10)
    btn.grid(row=row_value, column=col_value)
    btn.bind("<Button-1>", on_click)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1


window.mainloop()