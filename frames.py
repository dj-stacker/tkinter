import os
import time
import random
import string
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import threading

def openFileA():
    def open_file_thread():
        filename = filedialog.askopenfilename(
            initialdir="./",
            title="Open File A",
            filetypes=(("Text Files", "*.txt"),)
        )

        if filename:
            with open(filename, 'r') as file:
                data = file.read()

            data_text_A.delete('1.0', END)
            data_text_A.insert(END, data)

            unique_id = generate_unique_id()
            last_files[f"Filename_1_{unique_id}"] = filename
            last_datas[f"Data_1_{unique_id}"] = data

            print(f"File A {unique_id}", filename, data)

    threading.Thread(target=open_file_thread).start()

def openFileB():
    def open_file_thread():
        filename = filedialog.askopenfilename(
            initialdir="./",
            title="Open File B",
            filetypes=(("Text Files", "*.txt"),)
        )

        if filename:
            with open(filename, 'r') as file:
                data = file.read()

            data_text_B.delete('1.0', END)
            data_text_B.insert(END, data)

            unique_id = generate_unique_id()
            last_files[f"Filename_2_{unique_id}"] = filename
            last_datas[f"Data_2_{unique_id}"] = data

            print(f"File B {unique_id}", filename, data)

    threading.Thread(target=open_file_thread).start()

def handle_reverse(data_text):
    def reverse_thread():
        data = data_text.get('1.0', END).rstrip('\n')  # Remove trailing newline
        reversed_data = data[::-1]
        print("Reversed data:", reversed_data)
        reversed_text.delete('1.0', END)
        reversed_text.insert(END, reversed_data)
        reversed_text.mark_set("insert", "1.0")  # Set cursor position to the beginning

    threading.Thread(target=reverse_thread).start()

def generate_unique_id():
    timestamp = int(time.time())
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{timestamp}_{random_chars}"

def show_function_page(page):
    # Hide all frames
    frame_A.pack_forget()
    frame_B.pack_forget()
    frame_reversed.pack_forget()

    if page == "File A":
        frame_A.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
    elif page == "File B":
        frame_B.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
    elif page == "Reversed Text":
        frame_reversed.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

ws = tk.Tk()
ws.title("tkinter_reversed7.py")
ws.geometry("1300x550")
ws['bg'] = '#def8fc'

# Frame for File A
frame_A = tk.Frame(ws)
Label(frame_A, text="File A:", width=10).pack(side=TOP, padx=10, pady=5)
data_text_A = Text(frame_A, width=40, height=15)
data_text_A.pack(side=TOP, padx=10, pady=5)
Button(frame_A, text="Open", command=openFileA).pack(side=TOP, padx=10, pady=5)

# Frame for File B
frame_B = tk.Frame(ws)
Label(frame_B, text="File B:", width=10).pack(side=TOP, padx=10, pady=5)
data_text_B = Text(frame_B, width=40, height=15)
data_text_B.pack(side=TOP, padx=10, pady=5)
Button(frame_B, text="Open", command=openFileB).pack(side=TOP, padx=10, pady=5)

# Frame for Reversed Text
frame_reversed = tk.Frame(ws)
Label(frame_reversed, text="Reversed Text:", width=15).pack(side=TOP, padx=10, pady=5)
reversed_text = Text(frame_reversed, width=40, height=15)
reversed_text.pack(side=TOP, padx=10, pady=5)

# Initialize variables to store last file and data
last_files = {}
last_datas = {}

# Select Button Menu
select_button_menu = tk.StringVar()
select_button_menu.set("File A")  # Default selection

select_menu = OptionMenu(ws, select_button_menu, "File A", "File B", "Reversed Text", command=show_function_page)
select_menu.pack(side=TOP, padx=10, pady=10)

ws.mainloop()
