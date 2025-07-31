import tkinter as tk
from tkinter import messagebox
import glob
import main 

def generate_reports():
    files = glob.glob("data/*.csv")
    if not files:
        messagebox.showerror("Error", "No CSV files found in data/ folder")
        return
    
    try:
        main.file_processing(files)
        messagebox.showinfo("Success", "Financial statements generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

root = tk.Tk()
root.title("Financial Statement Generator")

tk.Label(root, text="Click button to generate financial statements from CSVs").pack(pady=10)
tk.Button(root, text="Generate", command=generate_reports).pack(pady=5)

root.mainloop()
