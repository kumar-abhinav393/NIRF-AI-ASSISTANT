import tkinter as tk
from tkinter import ttk, messagebox
from predict_ss import load_model, predict_ss

class SSCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="SS Calculator", padding=10)
        self.model = load_model()
        
        ttk.Label(self, text="Total Sanctioned Seats (NT_total): ").grid(row=0, column=0, sticky="w", pady=5)
        self.nt_entry = ttk.Entry(self, width=20)
        self.nt_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self, text="Total Enrolled Seats (NE_total): ").grid(row=1, column=0, sticky="w", pady=5)
        self.ne_entry = ttk.Entry(self, width=20)
        self.ne_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self, text="Total Enrolled PhD Seats (NP_total): ").grid(row=2, column=0, sticky="w", pady=5)
        self.np_entry = ttk.Entry(self, width=20)
        self.np_entry.grid(row=2, column=1, pady=5)
        
        predict_btn = ttk.Button(self, text="Predict_SS", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=3, column=0, sticky="w", padx=10)
        predict_btn.grid(row=3, column=1, sticky="e", padx=10)
        
        self.output_entry = ttk.Entry(self, width=25, font=("Ariel", 12, "bold"), state="readonly")
        self.output_entry.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    def predict_score(self):
        try:
            nt = float(self.nt_entry.get())
            ne = float(self.ne_entry.get())
            np = float(self.np_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
        
        if self.model is None:
            messagebox.showerror("Model Error", "SS Model not found")
            return
        
        try:
            score = predict_ss(self.model, nt, ne, np)
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, str(score))
            self.output_entry.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
    
    def clear_fields(self):
        self.nt_entry.delete(0, tk.END)
        self.ne_entry.delete(0, tk.END)
        self.np_entry.delete(0, tk.END)
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "")
        self.output_entry.config(state="readonly")