from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)


def button_clicked():
	new_text = float(input_field.get())
	label.config(text=f"is equal to {new_text * 1.6} Km")


button = Button(text="Calculate", command=button_clicked)
button.place(x=110, y=100)


input_field = Entry(width=20)
input_field.place(x=110, y=40)


#Labels
label = Label(text="is equal to 0 Km")
label.place(x=110, y=70)
miles = Label(text="Miles")
miles.place(x=200, y = 40)


window.mainloop()
