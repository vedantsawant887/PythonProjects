from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_symbols = [ random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list =  password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website_name :{
            "email":email,
            "password":password
        }
    }

    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")

    else:
        # is_ok = messagebox.askokcancel(title=website_name,message=f"These are the details entered:\n"
        #                                                           f"website: {website_name}\n"
        #                                                          f"email:{email}\npassword:{password}")
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json","w") as file:
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0,END)
            pass_entry.delete(0,END)

# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    website_name = website_entry.get()

    with open('data.json', 'r') as file:
        try:
            data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No data file found")
        else:
            if website_name in data:
                messagebox.showinfo(title=f"{website_name}", message=f"Email: {data[website_name]["email"]}\n"
                                                                    f"Password: {data[website_name]["password"]}")
            else:
                messagebox.showinfo(title="Oops", message=f"No details for the {website_name} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70 )



canvas = Canvas(window,height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(window,text="Website:")
website_label.grid(row=1,column=0)

website_entry = Entry(window,width=21,bg="white",fg="black")
website_entry.focus()
website_entry.grid(row=1,column=1)

search_button = Button(window,text="Search",bg="white",width=13,command=find_password)
search_button.grid(row=1,column=2)

email_label = Label(window,text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry = Entry(window,width=38,bg="white",fg="black")
email_entry.insert(0,"vedantsawant824@gmail.com")

email_entry.grid(row=2,column=1,columnspan=2)

pass_label = Label(window,text="Password:")
pass_label.grid(row=3,column=0)

pass_entry = Entry(window,width=21,bg="white",fg="black")

pass_entry.grid(row=3,column=1,)

generate_pass = Button(window,text="Generate Password",command=generate_password)
generate_pass.grid(row=3,column=2)

add_button = Button(window,text="Add",width=37,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()