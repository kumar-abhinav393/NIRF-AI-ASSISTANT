import tkinter as tk
from tkinter import ttk, messagebox

class FSRCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="FSR Calculator", padding=10)
        
        ttk.Label(self, text="Total Sanctioned Seats (NT_total): ").grid(row=0, column=0, sticky="w", pady=5)
        self.nt_entry = ttk.Entry(self, width=20)
        self.nt_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self, text="Permanen Enrolled PhD Seats (NP_total): ").grid(row=1, column=0, sticky="w", pady=5)
        self.ne_entry = ttk.Entry(self, width=20)
        self.ne_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self, text="Total Faculties (F_total): ").grid(row=2, column=0, sticky="w", pady=5)
        self.f_entry = ttk.Entry(self, width=20)
        self.f_entry.grid(row=2, column=1, pady=5)
        
        predict_btn = ttk.Button(self, text="Predict_FSR", command=self.predict_fsr)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=3, column=0, sticky="w", padx=10)
        predict_btn.grid(row=3, column=1, sticky="e", padx=10)
        
        self.output_entry = ttk.Entry(self, width=25, font=("Ariel", 12, "bold"), state="readonly")
        self.output_entry.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
    
    def predict_fsr(self):
        try:
            nt_total = float(self.nt_entry.get())
            np_total = float(self.ne_entry.get())
            f_total = float(self.f_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
        
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        # self.output_entry.insert(0, f"{fsr_score: .2f}")
        self.output_entry.config(state="readonly")
    
    def clear_fields(self):
        self.nt_entry.delete(0, tk.END)
        self.ne_entry.delete(0, tk.END)
        self.f_entry.delete(0, tk.END)
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "")
        self.output_entry.config(state="readonly")