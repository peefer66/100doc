
from random import randint,choice,shuffle
import itertools
from tkinter import *
from tkinter import messagebox

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','£','$','%','*']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
   # Create 3 lists of the different characters
    letters_list = [choice(letters) for char in range(randint(8, 10))] # 8 to 10 letters
    symbols_list = [choice(symbols) for char in range(randint(2, 4))] # 2 to 4 symbols
    numbers_list = [choice(numbers) for char in range(randint(2, 4))] # 2 to 4 numbers

    # user itertools.chain to combine the lists
    password_list = list(itertools.chain(letters_list,symbols_list,numbers_list))
    # shuffle to randomise
    shuffle(password_list)
    # Create a string from the password_list using the join() method
    password = ''.join(password_list)
    
    print(f"Your password is: {password}")
    # Populate the password_enty text box with the generated password
    password_entry.insert(0,password)
    

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_path = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 29 Password manager\Password\data.txt'
    
    # Get the text box entry details
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # vaidate contents
    if  len(website) != 0 and len(password) != 0: 
        # Confirm entry
        is_okay = messagebox.askokcancel(title=website,message=f'These are the details entered \n\n email: {email}\n password: {password}\n\n Okay to save?')
        
        if is_okay:
            with open(data_path,'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                # Delete the entries in the text boxes ready for the next
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    else:
        messagebox.showinfo(title='Validation Error',message='Please dont leave any fields empty')


# ---------------------------- UI SETUP ------------------------------- #
# Create the window and canvas

image_path = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 29 Password manager\Password\logo.png'
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=image_path)
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1,column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)
password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'peefer1966@gmail.com')
password_entry = Entry(width=30)
password_entry.grid(row=3,column=1)

# Buttons
generate_password_button = Button(text='Generate password',command=password_generator)
generate_password_button.grid(row=3,column=2)
add_button = Button(text='Add',width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()