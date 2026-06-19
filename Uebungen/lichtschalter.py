import tkinter as tk
import random

window = tk.Tk()
window.title("Lichtschalter")
window.geometry("300x250")

licht_an = False
wackel_aktiv = False
wackel_job = None

def aufgabe_generieren():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b, a + b

def licht_setzen(an):
    global licht_an
    licht_an = an
    if licht_an:
        window.config(bg="white")
        label.config(text="Licht an!", bg="white", fg="black")
        licht_button.config(text="Licht ausschalten")
        wackel_button.config(bg="white")
    else:
        window.config(bg="black")
        label.config(text="Licht aus!", bg="black", fg="white")
        licht_button.config(text="Licht einschalten")
        wackel_button.config(bg="SystemButtonFace")

def licht_toggle():
    licht_setzen(not licht_an)

def wackel_loop():
    global wackel_job
    if wackel_aktiv:
        licht_setzen(random.choice([True, False]))
        intervall = random.randint(1000, 5000)  # 1-5 Sekunden
        wackel_job = window.after(intervall, wackel_loop)

def wackelkontakt_click():
    a, b, antwort = aufgabe_generieren()

    popup = tk.Toplevel(window)
    popup.title("Kindersicherung")
    popup.geometry("250x180")
    popup.grab_set()

    tk.Label(popup, text="Löse die Aufgabe:", font=("Arial", 12)).pack(pady=10)

    aufgabe_label = tk.Label(popup, text=f"{a} + {b} = ?", font=("Arial", 14, "bold"))
    aufgabe_label.pack()

    eingabe_feld = tk.Entry(popup, font=("Arial", 12), justify="center")
    eingabe_feld.pack(pady=5)

    status_label = tk.Label(popup, text="", font=("Arial", 10), fg="red")
    status_label.pack()

    def pruefen():
        nonlocal a, b, antwort
        try:
            eingabe = int(eingabe_feld.get())
        except ValueError:
            status_label.config(text="Nur Zahlen eingeben!")
            return

        if eingabe == antwort:
            popup.destroy()
            wackel_starten()
        else:
            status_label.config(text="Falsch! Neue Aufgabe:")
            a, b, antwort = aufgabe_generieren()
            aufgabe_label.config(text=f"{a} + {b} = ?")
            eingabe_feld.delete(0, tk.END)

    tk.Button(popup, text="OK", command=pruefen, font=("Arial", 11)).pack(pady=5)

def wackel_starten():
    global wackel_aktiv, wackel_job
    if not wackel_aktiv:
        wackel_aktiv = True
        wackel_button.config(text="Wackelkontakt STOPPEN", fg="red")
        wackel_loop()
    else:
        wackel_aktiv = False
        if wackel_job:
            window.after_cancel(wackel_job)
        wackel_button.config(text="Wackelkontakt", fg="orange")

window.config(bg="black")

label = tk.Label(window, text="Licht aus!", bg="black", fg="white", font=("Arial", 14))
label.pack(expand=True)

licht_button = tk.Button(window, text="Licht einschalten", command=licht_toggle, font=("Arial", 12))
licht_button.pack(pady=5)

wackel_button = tk.Button(window, text="Wackelkontakt", command=wackelkontakt_click, font=("Arial", 10), fg="orange")
wackel_button.pack(pady=5)

window.mainloop()
