import tkinter as tk
 
window = tk.Tk()
window.title("GUI Mit Button")
window.geometry("200x100")
 
def on_click():
    label.config(text="Button geklickt")
 
button = tk.Button(window, text="Click me", command=on_click)
button.pack(padx=5, pady=5)
 
label = tk.Label(window, text="Warten auf den Klick")
label.pack(padx=5, pady=5)
 
   
window.mainloop()








# import tkinter as tk

# window = tk.Tk()
# window.title("Mein toller GUI")
# window.configure(bg="yellow")
# window.minsize(200, height=200)
# window.maxsize(500, height=500)

# widgets=[
#     tk.Label, tk.Checkbutton, tk. Entry, tk.Button, tk.Radiobutton, tk. Scale, tk.Spinbox
# ]

# for widget in widgets:
#     try:
#         w = widget(window, text=widget.__name__)
#     except tk.TclError:
#         w = widget(window)
        
#     w.pack(padx=5, pady=5, fill="x")
    
# window.mainloop()