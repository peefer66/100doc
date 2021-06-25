import tkinter as tk


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tk.Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = tk.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()