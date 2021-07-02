from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


entry = Entry()
entry.insert(END, string="0")
entry.grid(row=0, column=1)

Label(text="is equal to").grid(row=1, column=0)
km_label = Label(text="0")
km_label.grid(row=1, column=1)
Label(text="Miles", padx=10).grid(row=0,column=2)
Label(text="Km", padx=10).grid(row=1,column=2)

def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    km_label.config(text=f"{km:.2f}")

button = Button(text="Calculate", command=miles_to_km).grid(row=2, column=1)






window.mainloop()