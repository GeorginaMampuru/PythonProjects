import tkinter
import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image

# from tkinter import ttk
import json
import random

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

# creating custom tkinter window
app = customtkinter.CTk()
app.geometry("600x440")
app.title("Login - GUI")

img1 = ImageTk.PhotoImage(Image.open("CeedLogo.png"))

l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def clear_inputs():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry1_signup.delete(0, "end")
    entry2_signup.delete(0, "end")
    entry3_signup.delete(0, "end")


def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!!")
    elif username in signup_data and password == signup_data[username]["password"]:
        messagebox.showinfo("Successful", f"Welcome {username}")
        clear_inputs()
        open_banking_app()
    else:
        messagebox.showerror("Error", "Invalid User")


#   Load the sign-up data from the text file
def load_sign_up_data():
    try:
        with open("sign_up_data.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


#   when a user signs up, their details will be saved to the "sign_up_data.txt" file using JSON format.
#   When a user tries to log in, their credentials will be checked against the data loaded from the text file
def save_sign_up_data(data):
    with open("sign_up_data.txt", "w") as file:
        json.dump(data, file)


def sign_up():
    username = entry1_signup.get()
    password = entry2_signup.get()
    email = entry3_signup.get()

    if username == "" or password == "" or email == "":
        messagebox.showerror("Error", "All fields are required!!")
    else:
        signup_data[username] = {"password": password, "email": email}
        save_sign_up_data(signup_data)
        messagebox.showinfo("Success", "Sign up successful!")
        clear_inputs()


signup_data = load_sign_up_data()


def open_banking_app():
    def read_balance():
        try:
            with open("Bank Data.txt", "r") as file:
                balance = float(file.read())
        except (FileNotFoundError, ValueError):
            # Handle file not found or invalid value
            balance = 0.0  # Set a default balance value
        return balance

    def write_balance(balance):
        with open("Bank Data.txt", "w") as file:
            file.write(str(balance))

    def log_transaction(transaction):
        with open("Transaction Log.txt", "a") as file:
            file.write(transaction + "\n")

    def deposit():
        deposit_window = tk.Toplevel(root)
        deposit_window.title("Deposit")

        # Function to handle deposit button click
        def deposit_amount():
            try:
                amount = float(entry.get())
                if amount > 0:
                    balance = read_balance() + amount
                    write_balance(balance)
                    log_transaction("Deposit: +" + str(amount))
                    messagebox.showinfo("Success", "Deposit successful.")
                    balance_label.config(text="Current balance: R" + str(balance))
                    deposit_window.destroy()
                else:
                    messagebox.showerror(
                        "Error",
                        "Invalid amount. Deposit amount must be greater than zero.",
                    )
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid amount. Please enter a valid number."
                )

        deposit_label = tk.Label(
            deposit_window, text="How much would you like to deposit?"
        )
        deposit_label.pack(pady=10)
        entry = tk.Entry(deposit_window)
        entry.pack()

        deposit_button = tk.Button(
            deposit_window,
            text="Deposit",
            command=deposit_amount,
            bg="#4CAF50",
            fg="white",
            width=10,
            height=2,
            bd=0,
        )
        deposit_button.pack(pady=50)

        deposit_window.geometry("400x200")

    def withdraw():
        withdraw_window = tk.Toplevel(root)
        withdraw_window.title("Withdraw")

        # Function to handle withdraw button click
        def withdraw_amount():
            try:
                amount = float(entry.get())
                if amount > 0:
                    balance = read_balance()
                    if balance >= amount:
                        balance -= amount
                        write_balance(balance)
                        log_transaction("Withdrawal: -" + str(amount))
                        messagebox.showinfo("Success", "Withdrawal successful.")
                        balance_label.config(text="Current balance: R" + str(balance))
                        withdraw_window.destroy()
                    else:
                        messagebox.showerror("Error", "Insufficient funds.")
                else:
                    messagebox.showerror(
                        "Error",
                        "Invalid amount. Withdrawal amount must be greater than zero.",
                    )
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid amount. Please enter a valid number."
                )

        withdraw_label = tk.Label(
            withdraw_window, text="How much would you like to withdraw?"
        )
        withdraw_label.pack(pady=30)

        entry = tk.Entry(withdraw_window)
        entry.pack()

        withdraw_button = tk.Button(
            withdraw_window,
            text="Withdraw",
            command=withdraw_amount,
            bg="#F44336",
            fg="white",
            width=10,
            height=2,
            bd=0,
        )
        withdraw_button.pack(pady=30)

        withdraw_window.geometry("400x200")

    root = tk.Tk()
    root.title("Banking Application")
    root.iconbitmap("CeedLogo.ico")
    root.geometry("400x200")

  

    balance_label = tk.Label(
        root, text="Current balance: R" + str(read_balance()), font=("Helvetica", 16)
    )
    balance_label.pack(pady=20)

    deposit_button = tk.Button(
        root,
        text="Deposit",
        command=deposit,
        bg="#4CAF50",
        fg="white",
        width=10,
        height=2,
        bd=0,
    )
    deposit_button.pack(padx=15, pady=10)

    withdraw_button = tk.Button(
        root,
        text="Withdraw",
        command=withdraw,
        bg="#F44336",
        fg="white",
        width=10,
        height=2,
        bd=0,
    )
    withdraw_button.pack(padx=15, pady=10)

    root.mainloop()


l2 = customtkinter.CTkLabel(master=frame, text="Log in", font=("Century Gothic", 20))
l2.place(x=120, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(
    master=frame, width=220, placeholder_text="Password", show="*"
)
entry2.place(x=50, y=165)

l3 = customtkinter.CTkLabel(
    master=frame, text="Forget password?", font=("Century Gothic", 12)
)
l3.place(x=155, y=195)

# Create custom button
button1 = customtkinter.CTkButton(
    master=frame, width=220, text="Login", corner_radius=6, command=login
)
button1.place(x=50, y=240)


def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    length = 10
    password = "".join(random.sample(characters, length))
    return password


def open_signup_window():
    signup_window = customtkinter.CTkToplevel()
    signup_window.geometry("400x300")
    signup_window.title("Sign Up - GUI")

    global entry3_signup
    global entry1_signup
    global entry2_signup

    # Set the signup_window as a transient window to the main app window
    signup_window.transient(app)

    # Create the sign-up window
    label_username = customtkinter.CTkLabel(master=signup_window, text="Username:")
    label_username.pack()
    entry1_signup = customtkinter.CTkEntry(
        master=signup_window, width=320, placeholder_text="Enter your username"
    )
    entry1_signup.pack()

    def generate_and_update_password():
        generated_password = generate_password()
        entry2_signup.delete(0, tkinter.END)
        entry2_signup.insert(0, generated_password)

    button_generate_password = customtkinter.CTkButton(
        master=signup_window,
        text="Generate Password",
        width=280,
        corner_radius=6,
        command=generate_and_update_password,
    )
    button_generate_password.pack(pady=10)

    label_generated_password = customtkinter.CTkLabel(
        master=signup_window, text="Password:", font=("Century Gothic", 12)
    )
    label_generated_password.pack()

    entry2_signup = customtkinter.CTkEntry(
        master=signup_window,
        width=320,
        placeholder_text="Enter your password",
        show="*",
    )
    entry2_signup.pack()

    label_email = customtkinter.CTkLabel(master=signup_window, text="Email:")
    label_email.pack()
    entry3_signup = customtkinter.CTkEntry(
        master=signup_window, width=320, placeholder_text="Enter your email"
    )
    entry3_signup.pack()

    button_signup = customtkinter.CTkButton(
        master=signup_window, text="Sign Up", width=50, corner_radius=6, command=sign_up
    )
    button_signup.pack(padx=130, pady=30)


button2 = customtkinter.CTkButton(
    master=frame, width=220, text="Sign Up", corner_radius=6, command=open_signup_window
)
button2.place(x=50, y=280)

app.mainloop()
