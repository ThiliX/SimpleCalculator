import tkinter as tk

# Initial theme: Dark Mode
theme = {
    "bg": "#1e1e1e",
    "entry_bg": "#2d2d2d",
    "entry_fg": "white",
    "num_bg": "#333333",
    "num_fg": "white",
    "op_bg": "#ff9500",
    "op_fg": "white",
    "eq_bg": "#34c759",
    "eq_fg": "white",
    "c_bg": "#ff3b30",
    "c_fg": "white"
}

def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def toggle_theme():
    global theme
    if theme["bg"] == "#1e1e1e":  # Switch to light
        theme = {
            "bg": "#f0f0f0",
            "entry_bg": "#ffffff",
            "entry_fg": "black",
            "num_bg": "#e0e0e0",
            "num_fg": "black",
            "op_bg": "#ff9500",
            "op_fg": "white",
            "eq_bg": "#34c759",
            "eq_fg": "white",
            "c_bg": "#ff3b30",
            "c_fg": "white"
        }
    else:  # Switch to dark
        theme = {
            "bg": "#1e1e1e",
            "entry_bg": "#2d2d2d",
            "entry_fg": "white",
            "num_bg": "#333333",
            "num_fg": "white",
            "op_bg": "#ff9500",
            "op_fg": "white",
            "eq_bg": "#34c759",
            "eq_fg": "white",
            "c_bg": "#ff3b30",
            "c_fg": "white"
        }
    apply_theme()

def apply_theme():
    root.configure(bg=theme["bg"])
    entry.configure(bg=theme["entry_bg"], fg=theme["entry_fg"])
    for button, btn_type in button_widgets.items():
        if btn_type == "num":
            button.configure(bg=theme["num_bg"], fg=theme["num_fg"])
        elif btn_type == "op":
            button.configure(bg=theme["op_bg"], fg=theme["op_fg"])
        elif btn_type == "=":
            button.configure(bg=theme["eq_bg"], fg=theme["eq_fg"])
        elif btn_type == "C":
            button.configure(bg=theme["c_bg"], fg=theme["c_fg"])
    theme_button.configure(bg=theme["bg"], fg=theme["entry_fg"], relief="raised")

# Main window
root = tk.Tk()
root.title("Glassy Calculator")
root.geometry("350x450")
root.configure(bg=theme["bg"])

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5,
                 relief="ridge", justify="right", bg=theme["entry_bg"], fg=theme["entry_fg"])
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout
buttons = [
    ("7", "num"), ("8", "num"), ("9", "num"), ("/", "op"),
    ("4", "num"), ("5", "num"), ("6", "num"), ("*", "op"),
    ("1", "num"), ("2", "num"), ("3", "num"), ("-", "op"),
    ("0", "num"), (".", "num"), ("=", "="), ("+", "op"),
    ("C", "C")
]

button_widgets = {}
row_val = 1
col_val = 0

for text, btn_type in buttons:
    action = lambda x=text: click(x)
    btn = tk.Button(root, text=text, width=6, height=3, font=("Arial", 16),
                    command=action, relief="flat")
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    button_widgets[btn] = btn_type

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Theme toggle button
theme_button = tk.Button(root, text="Toggle Light/Dark", font=("Arial", 12),
                         command=toggle_theme)
theme_button.grid(row=row_val, column=0, columnspan=4, pady=10)

# Make buttons expand evenly
for i in range(row_val+1):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

apply_theme()
root.mainloop()
