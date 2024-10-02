import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = int(entry1.get())  
        num2 = int(entry2.get())  
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear():
    entry1.delete(0, tk.END)  
    entry2.delete(0, tk.END)  
    result_label.config(text="Result:")

def main():
    global entry1, entry2, result_label, operation_var 

    root = tk.Tk()
    root.title("Simple Python Calculator")
    
    root.geometry("400x400")
    root.config(bg="#e6e6e6")
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    vcmd = (root.register(validate_input), '%P')

    title_label = tk.Label(root, text="ARKA Calculator", font=("Arial", 18, "bold"), bg="#e6e6e6", fg="#333")
    title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

    label1 = tk.Label(root, text="Enter first number:", font=("Arial", 12), bg="#e6e6e6", fg="#333")
    label1.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry1 = tk.Entry(root, font=("Arial", 12), width=15, validate="key", validatecommand=vcmd)
    entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    label2 = tk.Label(root, text="Enter second number:", font=("Arial", 12), bg="#e6e6e6", fg="#333")
    label2.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry2 = tk.Entry(root, font=("Arial", 12), width=15, validate="key", validatecommand=vcmd)
    entry2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    operation_var = tk.StringVar(value="+")

    add_radio = tk.Radiobutton(root, text="Addition (+)", variable=operation_var, value="+", font=("Arial", 12), bg="#e6e6e6", fg="#333")
    add_radio.grid(row=3, column=0, padx=10, pady=5, sticky="e")

    sub_radio = tk.Radiobutton(root, text="Subtraction (-)", variable=operation_var, value="-", font=("Arial", 12), bg="#e6e6e6", fg="#333")
    sub_radio.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    mul_radio = tk.Radiobutton(root, text="Multiplication (*)", variable=operation_var, value="*", font=("Arial", 12), bg="#e6e6e6", fg="#333")
    mul_radio.grid(row=4, column=0, padx=10, pady=5, sticky="e")

    div_radio = tk.Radiobutton(root, text="Division (/)", variable=operation_var, value="/", font=("Arial", 12), bg="#e6e6e6", fg="#333")
    div_radio.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12), bg="#4CAF50", fg="white", width=12)
    calculate_button.grid(row=5, column=0, pady=20, padx=10, sticky="e")

    clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 12), bg="#f44336", fg="white", width=12)
    clear_button.grid(row=5, column=1, pady=20, padx=10, sticky="w")

    result_label = tk.Label(root, text="Result:", font=("Arial", 14), bg="#e6e6e6", fg="#333")
    result_label.grid(row=6, column=0, columnspan=2, pady=20, sticky="nsew")

    root.mainloop()

def validate_input(value):
    return value.isdigit() or value == "" 

if __name__ == "__main__":
    main()
