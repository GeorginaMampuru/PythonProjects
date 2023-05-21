import math
import tkinter as tk
from PIL import ImageTk, Image

def investment_calculator():
    amount = float(amount_entry.get())
    interest_rate = float(interest_entry.get()) / 100
    years = int(years_entry.get())
    interest_type = interest_var.get()

    if interest_type == "Simple":
        total_amount = amount * (1 + interest_rate * years)
    elif interest_type == "Compound":
        total_amount = amount * math.pow((1 + interest_rate), years)
    else:
        result_label["text"] = "Invalid interest type. Please select either 'Simple' or 'Compound'."
        return

    result_label["text"] = "Total amount after {} years: {:.2f}".format(years, total_amount)


def bond_calculator():
    present_value = float(present_value_entry.get())
    interest_rate = float(interest_entry.get())
    months = int(months_entry.get())

    monthly_interest_rate = (interest_rate / 100) / 12

    bond_repayment = (monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, -months))

    result_label["text"] = "Monthly bond repayment: {:.2f}".format(bond_repayment)


def calculate():
    choice = option_var.get()

    if choice == 1:
        investment_calculator()
    elif choice == 2:
        bond_calculator()
    else:
        result_label["text"] = "Invalid choice. Please select either 'Investment' or 'Bond'."


root = tk.Tk()
root.title("Finance Calculators")
root.geometry("600x600")

# Image
image = Image.open("CeedLogo1.png")  # Replace "image.jpg" with your image file path
image = image.resize((400, 200))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Investment Calculator
investment_frame = tk.Frame(root)
investment_frame.pack(pady=10)

amount_label = tk.Label(investment_frame, text="Amount:")
amount_label.grid(row=0, column=0)
amount_entry = tk.Entry(investment_frame)
amount_entry.grid(row=0, column=1)

interest_label = tk.Label(investment_frame, text="Interest (%):")
interest_label.grid(row=1, column=0)
interest_entry = tk.Entry(investment_frame)
interest_entry.grid(row=1, column=1)

years_label = tk.Label(investment_frame, text="Years:")
years_label.grid(row=2, column=0)
years_entry = tk.Entry(investment_frame)
years_entry.grid(row=2, column=1)

interest_type_label = tk.Label(investment_frame, text="Interest Type:")
interest_type_label.grid(row=3, column=0)
interest_var = tk.StringVar()
interest_var.set("Simple")
interest_type_dropdown = tk.OptionMenu(investment_frame, interest_var, "Simple", "Compound")
interest_type_dropdown.grid(row=3, column=1)

# Bond Calculator
bond_frame = tk.Frame(root)
bond_frame.pack(pady=10)

present_value_label = tk.Label(bond_frame, text="Present Value:")
present_value_label.grid(row=0, column=0)
present_value_entry = tk.Entry(bond_frame)
present_value_entry.grid(row=0, column=1)

interest_label = tk.Label(bond_frame, text="Interest (%):")
interest_label.grid(row=1, column=0)
interest_entry = tk.Entry(bond_frame)
interest_entry.grid(row=1, column=1)

months_label = tk.Label(bond_frame, text="Months:")
months_label.grid(row=2, column=0)
months_entry = tk.Entry(bond_frame)
months_entry.grid(row=2, column=1)

# Option Variable
option_var = tk.IntVar()

# Radio Buttons
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

investment_radio = tk.Radiobutton(radio_frame, text="Investment", variable=option_var, value=1)
investment_radio.pack(side="left")
bond_radio = tk.Radiobutton(radio_frame, text="Bond", variable=option_var, value=2)
bond_radio.pack(side="left")

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="blue", fg="white")
calculate_button.pack(pady=10)

root.mainloop()
