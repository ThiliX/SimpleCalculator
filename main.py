import tkinter as tk

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

# Main window
root = tk.Tk()
root.title("Dark Mode Calculator")
root.configure(bg="#1e1e1e")  # Dark background

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5,
                 relief="ridge", justify="right", bg="#2d2d2d", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click(x)

    # Style: different colors for operators, numbers, clear, etc.
    if button in {"+", "-", "*", "/"}:
        bg_color, fg_color = "#ff9500", "white"  # Orange for operators
    elif button == "=":
        bg_color, fg_color = "#34c759", "white"  # Green for equals
    elif button == "C":
        bg_color, fg_color = "#ff3b30", "white"  # Red for clear
    else:
        bg_color, fg_color = "#333333", "white"  # Dark gray for numbers

    tk.Button(root, text=button, width=5, height=2,
              font=("Arial", 16), command=action,
              bg=bg_color, fg=fg_color, relief="flat")\
        .grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make buttons expand evenly
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
