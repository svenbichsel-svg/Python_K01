import random
import tkinter as tk
from tkinter import messagebox
import threading

tipps = []
zusatz = None

def toggle_haupt(z):
    if len(tipps) == 6 and z not in tipps:
        return
    if z in tipps:
        tipps.remove(z)
        haupt_buttons[z].config(bg="#3c3c3c", fg="white")
    else:
        tipps.append(z)
        haupt_buttons[z].config(bg="gold", fg="black")

    if len(tipps) == 6:
        status_label.config(text="Jetzt Zusatzzahl wählen (1-6)!")
    else:
        status_label.config(text=f"Tipps ({len(tipps)}/6): {sorted(tipps)}")

def toggle_zusatz(z):
    global zusatz
    if zusatz == z:
        zusatz = None
        zusatz_buttons[z].config(bg="#3c3c3c", fg="white")
    else:
        if zusatz is not None:
            zusatz_buttons[zusatz].config(bg="#3c3c3c", fg="white")
        zusatz = z
        zusatz_buttons[z].config(bg="red", fg="white")
    status_label.config(text=f"Tipps: {sorted(tipps)} | Zusatz: {zusatz}")

def simulieren():
    if len(tipps) != 6 or zusatz is None:
        messagebox.showwarning("Fehler", "Bitte 6 Zahlen und eine Zusatzzahl wählen!")
        return

    # Ladebildschirm anzeigen
    lade_fenster = tk.Toplevel(fenster)
    lade_fenster.title("Simuliere...")
    lade_fenster.configure(bg="#1e1e1e")
    lade_fenster.geometry("300x150")
    lade_fenster.resizable(False, False)
    lade_fenster.grab_set()

    tk.Label(lade_fenster, text="🎰 Simulation läuft...",
             font=("Arial", 14, "bold"), bg="#1e1e1e", fg="white").pack(pady=20)

    versuch_label = tk.Label(lade_fenster, text="Versuche: 0",
                             font=("Arial", 11), bg="#1e1e1e", fg="yellow")
    versuch_label.pack()

    tk.Label(lade_fenster, text="Bitte warten...",
             font=("Arial", 9), bg="#1e1e1e", fg="gray").pack(pady=5)

    def simulation_thread():
        tipp_set = set(tipps)
        versuche = 0

        while True:
            versuche += 1
            ziehung = set()
            while len(ziehung) < 6:
                ziehung.add(random.randint(1, 42))
            z = random.randint(1, 6)

            # Alle 50'000 Versuche Anzeige aktualisieren
            if versuche % 50_000 == 0:
                versuch_label.config(text=f"Versuche: {versuche:,}".replace(",", "'"))

            if ziehung == tipp_set and z == zusatz:
                break

        # Fertig – Ladebildschirm schliessen und Ergebnis zeigen
        lade_fenster.destroy()

        kosten = versuche * 2.5
        alle = 5_245_786 * 6 * 2.5
        messagebox.showinfo("Ergebnis", (
            f"Ziehungen: {versuche:,}\n"
            f"Kosten (à CHF 2.50): CHF {kosten:,.2f}\n\n"
            f"Wahrscheinlichkeit: 1 zu {5_245_786 * 6:,}\n"
            f"Alle Tickets kaufen: CHF {alle:,.2f}"
        ).replace(",", "'"))

    thread = threading.Thread(target=simulation_thread, daemon=True)
    thread.start()

def reset():
    global zusatz
    tipps.clear()
    zusatz = None
    for btn in haupt_buttons.values():
        btn.config(bg="#3c3c3c", fg="white")
    for btn in zusatz_buttons.values():
        btn.config(bg="#3c3c3c", fg="white")
    status_label.config(text="Wähle 6 Zahlen (1-42)")

# Fenster
fenster = tk.Tk()
fenster.title("Schweizer Lotto")
fenster.configure(bg="#1e1e1e")

tk.Label(fenster, text="🎱 Schweizer Lotto", font=("Arial", 18, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

status_label = tk.Label(fenster, text="Wähle 6 Zahlen (1-42)",
                        font=("Arial", 11), bg="#1e1e1e", fg="yellow")
status_label.pack(pady=5)

tk.Label(fenster, text="Hauptzahlen (6 wählen)", font=("Arial", 10),
         bg="#1e1e1e", fg="gray").pack()
haupt_rahmen = tk.Frame(fenster, bg="#1e1e1e")
haupt_rahmen.pack(padx=20, pady=5)

haupt_buttons = {}
for i, z in enumerate(range(1, 43)):
    btn = tk.Button(haupt_rahmen, text=str(z), width=4, height=2,
                    bg="#3c3c3c", fg="white", font=("Arial", 10, "bold"),
                    relief="flat", cursor="hand2",
                    command=lambda z=z: toggle_haupt(z))
    btn.grid(row=i // 7, column=i % 7, padx=3, pady=3)
    haupt_buttons[z] = btn

tk.Label(fenster, text="Zusatzzahl (1-6)", font=("Arial", 10),
         bg="#1e1e1e", fg="gray").pack(pady=(10, 0))
zusatz_rahmen = tk.Frame(fenster, bg="#1e1e1e")
zusatz_rahmen.pack(pady=5)

zusatz_buttons = {}
for z in range(1, 7):
    btn = tk.Button(zusatz_rahmen, text=str(z), width=4, height=2,
                    bg="#3c3c3c", fg="white", font=("Arial", 10, "bold"),
                    relief="flat", cursor="hand2",
                    command=lambda z=z: toggle_zusatz(z))
    btn.grid(row=0, column=z - 1, padx=3, pady=3)
    zusatz_buttons[z] = btn

btn_rahmen = tk.Frame(fenster, bg="#1e1e1e")
btn_rahmen.pack(pady=10)

tk.Button(btn_rahmen, text="🎰 Simulation starten", font=("Arial", 11, "bold"),
          bg="#0078d4", fg="white", padx=10, pady=5, cursor="hand2",
          command=simulieren).grid(row=0, column=0, padx=5)

tk.Button(btn_rahmen, text="🔄 Reset", font=("Arial", 11),
          bg="#555", fg="white", padx=10, pady=5, cursor="hand2",
          command=reset).grid(row=0, column=1, padx=5)

fenster.mainloop()