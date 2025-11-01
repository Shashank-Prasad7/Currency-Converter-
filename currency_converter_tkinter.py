import tkinter as tk
from tkinter import ttk, messagebox

# Exchange Rate Data
# These rates are sample static values.
# You can later integrate an API for real-time data.
exchange_rates = {
    "USD": {"INR": 83.0, "EUR": 0.93, "USD": 1.0},
    "INR": {"USD": 0.012, "EUR": 0.011, "INR": 1.0},
    "EUR": {"USD": 1.08, "INR": 90.0, "EUR": 1.0}
}

# Currency Conversion Logic
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        # Perform conversion using predefined rates
        result = amount * exchange_rates[from_curr][to_curr]

        result_label.config(
            text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}",
            fg="white"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
    except KeyError:
        messagebox.showerror("Conversion Error", "Selected currency is not supported.")

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="#1c1c1c")  # Dark theme background


# Title Section
title_label = tk.Label(
    root,
    text="💱 Currency Converter 💱",
    font=("Helvetica", 16, "bold"),
    bg="#1c1c1c",
    fg="#00ffcc"
)
title_label.pack(pady=15)

# Input Field
input_frame = tk.Frame(root, bg="#1c1c1c")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Enter Amount:", fg="white", bg="#1c1c1c", font=("Arial", 11)).grid(row=0, column=0, padx=10)
amount_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
amount_entry.grid(row=0, column=1)

# Dropdown Menus
select_frame = tk.Frame(root, bg="#1c1c1c")
select_frame.pack(pady=10)

tk.Label(select_frame, text="From:", fg="white", bg="#1c1c1c", font=("Arial", 11)).grid(row=0, column=0, padx=5)
from_currency = ttk.Combobox(select_frame, values=list(exchange_rates.keys()), width=8, state="readonly")
from_currency.set("USD")
from_currency.grid(row=0, column=1, padx=5)

tk.Label(select_frame, text="To:", fg="white", bg="#1c1c1c", font=("Arial", 11)).grid(row=0, column=2, padx=5)
to_currency = ttk.Combobox(select_frame, values=list(exchange_rates.keys()), width=8, state="readonly")
to_currency.set("INR")
to_currency.grid(row=0, column=3, padx=5)

# Convert Button
convert_button = tk.Button(
    root,
    text="Convert",
    command=convert_currency,
    font=("Arial", 12, "bold"),
    bg="#00cc66",
    fg="white",
    activebackground="#00e673",
    relief="raised",
    bd=3,
    padx=10,
    pady=5
)
convert_button.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg="#1c1c1c",
    fg="white"
)
result_label.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Developed by Shashank | Tkinter Project",
    font=("Arial", 9, "italic"),
    fg="#999999",
    bg="#1c1c1c"
)
footer.pack(side="bottom", pady=10)

# Run Application
root.mainloop()
