import tkinter as tk
from tkinter import scrolledtext

# Function for Caesar cipher encryption/decryption
def caesar_cipher(text, shift, direction):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if direction == 'R' else -shift
            if char.isupper():
                result += chr(((ord(char) - 65 + shift_amount) % 26) + 65)
            else:
                result += chr(((ord(char) - 97 + shift_amount) % 26) + 97)
        else:
            result += char
    return result

# Function to handle encryption or decryption
def process_text():
    input_text = input_text_entry.get()
    operation = operation_var.get()
    direction = direction_var.get()
    shift = shift_entry.get()
    
    if shift.isdigit():
        shift = int(shift)
        if operation == 'E':
            result = caesar_cipher(input_text, shift, direction)
            output_text.delete(1.0, tk.END)  # Clear previous output
            output_text.insert(tk.END, result)
        elif operation == 'D':  # Add decryption logic
            result = caesar_cipher(input_text, shift, direction)
            output_text.delete(1.0, tk.END)  # Clear previous output
            output_text.insert(tk.END, result)
    else:
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, "Invalid shift value. Please enter a positive integer.")

# Function to clear all text fields and options
def clear_all():
    input_text_entry.delete(0, tk.END)  # Clear input text
    output_text.delete(1.0, tk.END)     # Clear output text
    operation_var.set("")               # Clear operation option
    direction_var.set("")               # Clear direction option
    shift_entry.delete(0, tk.END)       # Clear shift value

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher Encryption/Decryption")
window.geometry("800x500")  # Increase the window height

# Create and configure widgets
input_label = tk.Label(window, text="Enter text:", font=("Helvetica", 14, "bold"))
input_label.pack(pady=10)

input_text_entry = tk.Entry(window, width=70, font=("Helvetica", 12))
input_text_entry.pack(fill=tk.X, padx=20)

operation_var = tk.StringVar()
operation_var.set("")  # Initialize with an empty string

operation_label = tk.Label(window, text="Select operation:", font=("Helvetica", 14, "bold"))
operation_label.pack(pady=5)

operation_frame = tk.Frame(window)
operation_frame.pack()

encrypt_radio = tk.Radiobutton(operation_frame, text="Encryption", variable=operation_var, value="E", indicatoron=False, font=("Helvetica", 12))
decrypt_radio = tk.Radiobutton(operation_frame, text="Decryption", variable=operation_var, value="D", indicatoron=False, font=("Helvetica", 12))
encrypt_radio.pack(side=tk.LEFT, padx=10)
decrypt_radio.pack(side=tk.LEFT, padx=10)

direction_var = tk.StringVar()
direction_var.set("")  # Initialize with an empty string

direction_label = tk.Label(window, text="Select direction:", font=("Helvetica", 14, "bold"))
direction_label.pack(pady=5)

direction_frame = tk.Frame(window)
direction_frame.pack()

right_shift_radio = tk.Radiobutton(direction_frame, text="Right Shift", variable=direction_var, value="R", indicatoron=False, font=("Helvetica", 12))
left_shift_radio = tk.Radiobutton(direction_frame, text="Left Shift", variable=direction_var, value="L", indicatoron=False, font=("Helvetica", 12))
right_shift_radio.pack(side=tk.LEFT, padx=10)
left_shift_radio.pack(side=tk.LEFT, padx=10)

shift_label = tk.Label(window, text="Enter shift number:", font=("Helvetica", 14, "bold"))
shift_label.pack(pady=5)

shift_entry = tk.Entry(window, width=5, font=("Helvetica", 12))
shift_entry.pack()

process_button = tk.Button(window, text="Process", command=process_text, font=("Helvetica", 14, "bold"))
process_button.pack(pady=10)

clear_all_button = tk.Button(window, text="Clear All", command=clear_all, font=("Helvetica", 14, "bold"))
clear_all_button.pack(pady=10)

output_label = tk.Label(window, text="Result:", font=("Helvetica", 14, "bold"))
output_label.pack(pady=10)

output_text = scrolledtext.ScrolledText(window, height=10, width=70, font=("Helvetica", 12))
output_text.pack(fill=tk.BOTH, padx=20, pady=10)

# Start the Tkinter main loop
window.mainloop()
