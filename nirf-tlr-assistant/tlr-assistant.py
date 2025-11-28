import os
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import google.generativeai as genai
from helpers.build_prompt import build_prompt
from helpers.spinner import (start_spinner, stop_spinner)
from helpers.ansi_color_codes import (COLOR_ERROR, COLOR_HEADER, COLOR_INFO,
    COLOR_OK, COLOR_RESET, COLOR_WARNING)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
else:
    gemini_model = None

def create_input_frame(root):
    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="x")
    
    labels = [
        "Total Students",
        "Total Faculty",
        "PhD Faculty",
        "PhD Students",
        "Annual Expenditure(in crore)",
        "Seat Occupancy (%)",
    ]
    
    entries = {}

    institute_header = ttk.Label(frame, text="Institute Data", font=("Arial", 12, "bold"))
    institute_header.grid(row=0, column=0, sticky="w", pady=(0,5))
    
    for i, label_text in enumerate(labels):
        label = ttk.Label(frame, text=label_text)
        label.grid(row=i+1, column=0, sticky="w", pady=5)
        
        entry = ttk.Entry(frame, width=30)
        entry.grid(row=i+1, column=1, sticky="w", pady=5, padx=10)
        
        entries[label_text] = entry

    separator = ttk.Separator(frame, orient="horizontal")
    separator.grid(row=7, column=0, columnspan=2, sticky="we", pady=10)

    goal_header = ttk.Label(frame, text="Goal Settings", font=("Arial", 12, "bold"))
    goal_header.grid(row=8, column=0, sticky="w", pady=(0,5))

    target_label = ttk.Label(frame, text="Target TLR Score")
    target_label.grid(row=9, column=0, sticky="w", pady=5)
    target_entry = ttk.Entry(frame, width=30)
    target_entry.grid(row=9, column=1, sticky="w", pady=5, padx=10)
    entries["Target TLR Score"] = target_entry
    
    return frame, entries

def create_output_box(root):
    output_label = ttk.Label(root, text="Output:")
    output_label.pack(anchor="w", padx=10)
    
    output_text = tk.Text(root, wrap="word", height=20)
    output_text.pack(fill="both", expand=True, padx=10, pady=10)
    
    return output_text

def collect_input_values(entries):
    total_students = int(entries["Total Students"].get())
    total_faculty = int(entries["Total Faculty"].get())
    phd_faculty = int(entries["PhD Faculty"].get())
    phd_students = int(entries["PhD Students"].get())
    annual_expenditure = float(entries["Annual Expenditure(in crore)"].get())
    occupancy = int(entries["Seat Occupancy (%)"].get())
    target_tlr_score = int(entries["Target TLR Score"].get())
    
    return {
        "total_students": total_students,
        "total_faculty": total_faculty,
        "phd_faculty": phd_faculty,
        "phd_students": phd_students,
        "annual_expenditure": annual_expenditure,
        "occupancy": occupancy,
        "target_score": target_tlr_score,
    }

def call_gemini(prompt: str) -> str:
    if not gemini_model:
        raise RuntimeError("GEMINI_API_KEY env variable not set.")
    
    response = gemini_model.generate_content(prompt)
    return response.text

def handle_submit(entries, output_text, root):
    try:
        values = collect_input_values(entries)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    prompt = build_prompt(values)

    print(f"{COLOR_INFO}[Gemini] Generated prompt:{COLOR_RESET}\n{prompt}")

    start_spinner(root, output_text)

    def worker():
        try:
            answer = call_gemini(prompt)
            result_text = f"✅ Gemini Response:\n\n{answer}"
            print(f"{COLOR_OK}[Gemini] Response received successfully.{COLOR_RESET}")
        except Exception as e:
            result_text = f"❌ Error calling Gemini API:\n{e}"
            print(f"{COLOR_ERROR}[Gemini] Error: {e}{COLOR_RESET}")

        def update_ui():
            stop_spinner()
            output_text.delete("1.0", "end")
            output_text.insert("1.0", result_text)

        root.after(0, update_ui)

    threading.Thread(target=worker, daemon=True).start()

def create_submit_button(root, entries, output_text):
    button = ttk.Button(
        root,
        text="Get TLR Recommendation",
        command=lambda: handle_submit(entries, output_text, root)
    )
    button.pack(pady=15)

def main():
    root = tk.Tk()
    root.title("NIRF TLR Assistant")
    root.geometry("900x900")
    
    input_frame, entries = create_input_frame(root)
    output_text = create_output_box(root)
    create_submit_button(root, entries, output_text)
    
    print(input_frame)
    print(output_text)

    root.mainloop()

if __name__ == "__main__":
    main()