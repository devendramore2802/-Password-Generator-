import customtkinter as ctk
import random
import string
import pyperclip

# Window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔐 Password Generator V2")
app.geometry("500x450")
app.resizable(False, False)

# Title
title = ctk.CTkLabel(
    app,
    text="🔐 Password Generator",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

# Length Label
length_label = ctk.CTkLabel(app, text="Password Length")
length_label.pack()

length_entry = ctk.CTkEntry(app, width=120)
length_entry.insert(0, "12")
length_entry.pack(pady=10)

# Result Box
result = ctk.CTkEntry(app, width=350, height=40, font=("Arial", 18))
result.pack(pady=20)

# Strength Label
strength = ctk.CTkLabel(app, text="")
strength.pack()

# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for i in range(length))

        result.delete(0, "end")
        result.insert(0, password)

        if length < 8:
            strength.configure(text="🔴 Weak Password")
        elif length < 12:
            strength.configure(text="🟡 Medium Password")
        else:
            strength.configure(text="🟢 Strong Password")

    except:
        result.delete(0, "end")
        result.insert(0, "Enter Valid Number")

# Copy Password
def copy_password():
    pyperclip.copy(result.get())
    strength.configure(text="✅ Password Copied!")

# Buttons
generate_btn = ctk.CTkButton(
    app,
    text="Generate Password",
    command=generate_password,
    width=220
)
generate_btn.pack(pady=10)

copy_btn = ctk.CTkButton(
    app,
    text="Copy Password",
    command=copy_password,
    width=220
)
copy_btn.pack()

app.mainloop()