import tkinter as tk

# Window
window = tk.Tk()
window.minsize(width=250, height=100)
window.title('Miles to KM Converter')
window.config(padx=20, pady=20)

# input box
miles_input = tk.Entry()
miles_input.insert(tk.END, string=0)
miles_input.grid(column=2, row=0)
miles_input.config(width=10)

#Label - 
label_0 = tk.Label(text='Miles')
label_0.grid(column=3, row=0)

label_1 = tk.Label(text='Is equal to')
label_1.grid(column=1,row=1)

label_2 = tk.Label()
label_2.grid(column=2,row=1)

label_3 = tk.Label(text='kilometers')
label_3.grid(column=3, row=1)

# Button
def calculate():
    miles_input.get()
    # Convert to KM rounded to 1d.p
    miles_to_km = round(float(miles_input.get()) * 1.6,1)
    label_2.config(text=miles_to_km)

button_calculate = tk.Button(text='Calculate',command=calculate)
button_calculate.grid(column=2,row=2)







window.mainloop()