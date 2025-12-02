import tkinter as tk
from tkinter import ttk, messagebox

class FQECalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="FQE Calculator", padding=10)
    
        ttk.Label(self, text="Total Actual Faculty (F_total): ").grid(row=0, column=0, sticky="w", pady=5)
        self.f_total_entry = ttk.Entry(self, width=20)
        self.f_total_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self, text="Total Required Faculty (F_required): ").grid(row=1, column=0, sticky="w", pady=5)
        self.f_required_entry = ttk.Entry(self, width=20)
        self.f_required_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self, text="Faculty with PhD (PhD_faculty): ").grid(row=2, column=0, sticky="w", pady=5)
        self.phd_faculty_entry = ttk.Entry(self, width=20)
        self.phd_faculty_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(self, text="Faculty experience ≤ 8 years (Exp1_count): ").grid(row=3, column=0, sticky="w", pady=5)
        self.exp1_entry = ttk.Entry(self, width=20)
        self.exp1_entry.grid(row=3, column=1, pady=5)
        
        ttk.Label(self, text="Faculty experience 8–15 years (Exp2_count): ").grid(row=4, column=0, sticky="w", pady=5)
        self.exp2_entry = ttk.Entry(self, width=20)
        self.exp2_entry.grid(row=4, column=1, pady=5)
        
        ttk.Label(self, text="Faculty experience > 15 years (Exp3_count): ").grid(row=5, column=0, sticky="w", pady=5)
        self.exp3_entry = ttk.Entry(self, width=20)
        self.exp3_entry.grid(row=5, column=1, pady=5)
        
        predict_btn = ttk.Button(self, text="Predict FQE", command=self.predict_fqe)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=6, column=0, sticky="w", padx=10)
        predict_btn.grid(row=6, column=1, sticky="e", padx=10)
        
        self.output_entry = ttk.Entry(self, width=25, font=("Ariel", 12, "bold"), state="readonly")
        self.output_entry.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")
        
    def predict_fqe(self):
        pass
    
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.config(state="readonly")
            
    def clear_fields(self):
        self.f_total_entry.delete(0, tk.END)
        self.f_required_entry.delete(0, tk.END)
        self.phd_faculty_entry.delete(0, tk.END)
        self.exp1_entry.delete(0, tk.END)
        self.exp2_entry.delete(0, tk.END)
        self.exp3_entry.delete(0, tk.END)
        self.output_label.config(text="")