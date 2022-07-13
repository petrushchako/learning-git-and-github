from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background = "light blue")
window.geometry("320x220")
window.resizable(width=True, height=True)

ft_lbl = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

mt_lbl=Label(window, text="Meter", bg="blue", fg="white", width=14)
mt_lbl.grid(column=0, row=1, padx=15, pady=15)

conv_lbl=label(window, text="Clear", bg="green", fg="white", width=14)
conv_lbl.grid(column=0, row=2, padx=15, pady=15)

clr_lbl=Label(window, text="Convert", bg="red", fg="green", width=14)
clr_lbl.grid(column=1, row=2, padx=15, pady=15)

window.mainloop()
