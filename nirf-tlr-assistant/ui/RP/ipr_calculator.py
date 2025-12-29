import tkinter as tk
from tkinter import ttk, messagebox

class IPRCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="IPR Calculation", padding=10)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        
        style = ttk.Style()
        style.configure("Docs.TButton", 
                       background="#4A90E2", 
                       foreground="#FFFFFF",
                       font=("Arial", 10, "bold"),
                       padding=5)
        
        btn_docs = ttk.Button(self, text="📘 IPR Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: PatGranted(Year 1), PatGranted(Year 2), PatGranted(Year 3)
        ttk.Label(self, text="Pat Garnted(Year 1):").grid(row=1, column=0, sticky="w", padx=2, pady=5)
        self.pat_granted1 = ttk.Entry(self, width=10)
        self.pat_granted1.grid(row=1, column=1, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Pat Garnted(Year 2):").grid(row=1, column=2, sticky="w", padx=2, pady=5)
        self.pat_granted2 = ttk.Entry(self, width=10)
        self.pat_granted2.grid(row=1, column=3, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Pat Garnted(Year 3):").grid(row=1, column=4, sticky="w", padx=2, pady=5)
        self.pat_granted3 = ttk.Entry(self, width=10)
        self.pat_granted3.grid(row=1, column=5, sticky="ew", padx=2, pady=5)
        
        # Row 2: PatPublished(Year 1), PatPublished(Year 2), PatPublished(Year 3)
        ttk.Label(self, text="Pat Published(Year 1):").grid(row=2, column=0, sticky="w", padx=2, pady=5)
        self.pat_published1 = ttk.Entry(self, width=10)
        self.pat_published1.grid(row=2, column=1, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Pat Published(Year 2):").grid(row=2, column=2, sticky="w", padx=2, pady=5)
        self.pat_published2 = ttk.Entry(self, width=10)
        self.pat_published2.grid(row=2, column=3, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Pat Published(Year 3):").grid(row=2, column=4, sticky="w", padx=2, pady=5)
        self.pat_published3 = ttk.Entry(self, width=10)
        self.pat_published3.grid(row=2, column=5, sticky="ew", padx=2, pady=5)
        
        # Row 3: Buttons
        predict_btn = ttk.Button(self, text="Predict IPR")
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=2, pady=5)
        predict_btn.grid(row=3, column=3, columnspan=3, sticky="ew", padx=2, pady=5)
        
        # Row 4: Output and recommendation
        self.output_entry = ttk.Entry(self, width=15, font=("Ariel", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2, pady=(0, 15))
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "IPR Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get IPR Recommendation")
        recommend_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2, pady=(0, 15))