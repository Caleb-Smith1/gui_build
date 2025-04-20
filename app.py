import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# 🔒 Load .env from same folder
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# DEBUG — print API key (REMOVE AFTER TESTING)
print("API Key loaded from .env:", os.getenv("OPENAI_API_KEY"))

# 🔐 Connect to OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to fetch AI response
def get_completion():
    prompt = prompt_input.get("1.0", tk.END).strip()
    if prompt:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content.strip()
        except Exception as e:
            result = f"Error: {e}"

        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state='disabled')

# Build GUI
window = tk.Tk()
window.title("OpenAI Prompt App")
window.geometry("600x500")

tk.Label(window, text="Enter your prompt:").pack(pady=5)

prompt_input = tk.Text(window, height=5, width=70)
prompt_input.pack(pady=5)

tk.Button(window, text="Submit", command=get_completion).pack(pady=5)

tk.Label(window, text="Output:").pack(pady=5)

output_box = scrolledtext.ScrolledText(window, height=12, width=70, state='disabled')
output_box.pack(pady=5)

window.mainloop()
