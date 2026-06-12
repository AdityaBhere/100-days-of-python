from tkinter import *

screen = Tk()
screen.title("Miles to Km Converter")
screen.minsize(width=100,height=100)
screen.config(padx=10,pady=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5,pady=5)

is_equal_to_label = Label(text="is equals to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=5,pady=5)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5,pady=5)

km_equal_to_label = Label(text="0")
km_equal_to_label.grid(column=1, row=1)
km_equal_to_label.config(padx=5, pady=5)

miles_entry = Entry()
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)


def calculate():
    miles = float(miles_entry.get())
    km = miles * 1.6
    km_equal_to_label.config(text=round(km))

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


screen.mainloop()