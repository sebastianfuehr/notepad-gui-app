import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu, filedialog, messagebox

root = tk.Tk()
root.title('Notes')

textarea = ScrolledText(root)
textarea.pack()

menu = Menu(root)
file = Menu(menu, tearoff=0)

def open_file():
    print('Open File')
    root.filename = filedialog.askopenfilename(
        initialdir='~',
        title='Select File',
        filetypes=(('jpeg files', '*.jpg'), ('all files', '*.*'))
    )
    file = open(root.filename)
    textarea.insert('end', file.read())

def save_file():
    pass

def save_file_as():
    root.filename = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if root.filename is None:
        return
    file_to_save = str(textarea.get(1.0, tk.END))
    root.filename.write(file_to_save)
    root.filename.close()

def exit():
    message = messagebox.askquestion('Notepad', 'Do you want to save?')
    if message == 'yes':
        save_file_as()
    root.destroy()

file.add_command(label='Open', command=open_file)
file.add_command(label='Save', command=save_file)
file.add_command(label='Save As', command=save_file_as)
file.add_separator()
file.add_command(label='Exit', command=exit)

menu.add_cascade(label='File', menu=file)
root.config(menu=menu)

root.mainloop()