import tkinter as tk
import google.generativeai as genai
import os
import sys

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set it before running. Get a key from aistudio.google.com")
    sys.exit(1)
genai.configure(api_key=API_KEY)

def simulate_thinking():
    prompt = prompt_entry.get()
    if not prompt:
        output_label.config(text="Enter a prompt.")
        return

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Describe what a simple image based on this text prompt would visually represent or suggest related visual elements (be brief): '{prompt}'", safety_settings=[{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},])

        output_text = response.text
        output_label.config(text=f"Thinker's idea:\n{output_text}")

    except Exception as e:
        output_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("AI Text Idea Generator (Thinker)")

tk.Label(root, text="Enter Image Idea Prompt:").pack(pady=5)
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=5)

tk.Button(root, text="Simulate Thinking Process", command=simulate_thinking).pack(pady=10)

output_label = tk.Label(root, text="", wraplength=400, justify="left")
output_label.pack(pady=10)

root.mainloop()
