import tkinter as tk
from tkinter import ttk, messagebox

class FRUCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="FRU Calculator", padding=10)
    
        ttk.Label(self, text="Capital Expenditure Year 1 (CE1_total): ").grid(row=0, column=0, sticky="w", pady=5)
        self.ce1_total_entry = ttk.Entry(self, width=20)
        self.ce1_total_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self, text="Capital Expenditure Year 2 (CE2_total): ").grid(row=1, column=0, sticky="w", pady=5)
        self.ce2_total_entry = ttk.Entry(self, width=20)
        self.ce2_total_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self, text="Capital Expenditure Year 3 (CE3_total): ").grid(row=2, column=0, sticky="w", pady=5)
        self.ce3_total_entry = ttk.Entry(self, width=20)
        self.ce3_total_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(self, text="Operational Expenditure Year 1 (OE1_total): ").grid(row=3, column=0, sticky="w", pady=5)
        self.oe1_total_entry = ttk.Entry(self, width=20)
        self.oe1_total_entry.grid(row=3, column=1, pady=5)
        
        ttk.Label(self, text="Operational Expenditure Year 2 (OE2_total): ").grid(row=4, column=0, sticky="w", pady=5)
        self.oe2_total_entry = ttk.Entry(self, width=20)
        self.oe2_total_entry.grid(row=4, column=1, pady=5)
        
        ttk.Label(self, text="Operational Expenditure Year 3 (OE3_total): ").grid(row=5, column=0, sticky="w", pady=5)
        self.oe3_total_entry = ttk.Entry(self, width=20)
        self.oe3_total_entry.grid(row=5, column=1, pady=5)
        
        predict_btn = ttk.Button(self, text="Predict FRU", command=self.predict_fru)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=6, column=0, sticky="w", padx=10)
        predict_btn.grid(row=6, column=1, sticky="e", padx=10)
        
        self.output_entry = ttk.Entry(self, width=25, font=("Ariel", 12, "bold"), state="readonly")
        self.output_entry.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")
        
    def predict_fru(self):
        pass
    
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.config(state="readonly")
            
    def clear_fields(self):
        self.ce1_total_entry.delete(0, tk.END)
        self.ce2_total_entry.delete(0, tk.END)
        self.ce3_total_entry.delete(0, tk.END)
        self.oe1_total_entry.delete(0, tk.END)
        self.oe2_total_entry.delete(0, tk.END)
        self.oe3_total_entry.delete(0, tk.END)
        self.output_entry.config(text="")