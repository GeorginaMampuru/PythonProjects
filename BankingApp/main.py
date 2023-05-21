import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *

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
                messagebox.showerror("Error", "Invalid amount. Deposit amount must be greater than zero.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
    
    deposit_label = tk.Label(deposit_window, text="How much would you like to deposit?")
    deposit_label.pack(pady=10)
    
    entry = tk.Entry(deposit_window)
    entry.pack()
    
    deposit_button = tk.Button(deposit_window, text="Deposit", command=deposit_amount, bg="#4CAF50", fg="white", width=10, height=2, bd=0)
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
                messagebox.showerror("Error", "Invalid amount. Withdrawal amount must be greater than zero.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
    
    withdraw_label = tk.Label(withdraw_window, text="How much would you like to withdraw?")
    withdraw_label.pack(pady=30)
    
    entry = tk.Entry(withdraw_window)
    entry.pack()
    
    withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=withdraw_amount, bg="#F44336", fg="white", width=10, height=2, bd=0)
    withdraw_button.pack(pady=30)
    
    withdraw_window.geometry("400x200")

root = tk.Tk()
root.title("Banking Application")
root.iconbitmap("CeedLogo.ico")
root.geometry("600x600")

# Load and display image
image = Image.open("CeedLogo1.png")
image = image.resize((400, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg="black")
image_label.pack(pady=20)

balance_label = tk.Label(root, text="Current balance: R" + str(read_balance()), font=("Helvetica", 16))
balance_label.pack(pady=20)

deposit_button = tk.Button(root, text="Deposit", command=deposit, bg="#4CAF50", fg="white", width=10, height=2, bd=0)
deposit_button.pack(pady=10)
deposit_button.pack(padx=15)

withdraw_button = tk.Button(root, text="Withdraw", command=withdraw, bg="#F44336", fg="white", width=10, height=2, bd=0)
withdraw_button.pack(pady=10)
withdraw_button.pack(padx=15)

root.mainloop()
