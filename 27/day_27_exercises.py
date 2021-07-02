from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

# Update properties
my_label["text"] = "New label"
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    if new_text != "":
        my_label.config(text = new_text)
    # my_label.config(text="Button Got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Entry 
input = Entry(width=10)
input.grid(row=2, column=3)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

window.mainloop()

# Layout managers (pack(), place(), grid())
# Place
my_label.place(x=0, y=0) # places label at the top left corner
my_label.place(x=100, y=100) # x moves to right, y moves down

# Grid
my_label.grid(column=0, row=0) # top left