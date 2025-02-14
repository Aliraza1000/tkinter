import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Product: {result}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Invalid input! Please enter numbers.")
root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")
desc_label = tk.Label(root, text="This application multiplies two numbers.", font=("Arial", 10))
desc_label.pack(pady=5)
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=10)
result_box = tk.Text(root, height=2, width=30)
result_box.pack()
root.mainloop()