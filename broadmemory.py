from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk

root = Tk()
root.option_add('*Font', 'Tomapip install Pillow')
root.configure(bg = "#C5DECD")
root.title("Create Account")







image = Image.open(r"C:\Users\jaybr\OneDrive\Documents\13 DDT - Jay\signup_button.png")
resized_image = image.resize((20, 20))

photo = ImageTk.PhotoImage(resized_image)

label = Label(root, image=photo)
label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

account = PhotoImage(file=r"C:\Users\jaybr\OneDrive\Documents\13 DDT - Jay\loginiamge.png")
account_label = Label(root, image=account, background="#C5DECD")
account_label.grid(row=1, column=0, padx=10, pady=(10,50), columnspan=2)


clickhere = ttk.Label(root, text="Sign in to Continue.", font=customtkinter.CTkFont(size=12, weight="bold"), foreground="#185cac", background="#C5DECD")
clickhere.place(x=138,y=232)

username_label = ttk.Label(root, text="Username:", foreground="#1871ac", background="#C5DECD", font=('Georgia', 13, 'bold'))
username_label.grid(row=3, column=0,  pady=5)
username_entry = customtkinter.CTkEntry(root, width=300)
username_entry.grid(row=3, column=1, pady=5)


password_label = ttk.Label(root, text="Password:", foreground="#1871ac", background="#C5DECD", font=('Georgia', 13, 'bold'))
password_label.grid(row=5, column=0,pady=5)
password_entry = customtkinter.CTkEntry(root, show="", width=300)
password_entry.grid(row=5, column=1,  pady=5)





def register_user():
    username = username_entry.get()
   
    password = password_entry.get()
    

    
    message_label.config(text="User registered successfully!", foreground="green")



login = customtkinter.CTkButton(root, text="Sign in", font=customtkinter.CTkFont(family="Kaiti", size=16),)
login.grid(row=7, column=0, padx=10, pady=10, columnspan=2)
message_label = ttk.Label(root, text="", foreground="red", background="#C5DECD", font=('Arial', 12, 'bold'))
message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)

root.mainloop()

# Create an Entry widget

root.mainloop()
