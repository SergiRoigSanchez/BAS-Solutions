from tkinter import *

root = Tk()
root.title('Title')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry ("400x400")

my_menu = Menu (root)
root.config(menu=my_menu)

# Click command 
def test_command():
    my_label = Label(root, text="Prova").pack()

# Funció File new
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text="Has clicat el menú File >> New").pack()

# Funció Edit cut
def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(edit_cut_frame, text="Has clicat el menú Edit >> Cut").pack()

# Amaga tots els frames
def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

# Objectes de menú
file_menu = Menu (my_menu)
my_menu.add_cascade(label="File", menu=file_menu) 
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu (my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=test_command)

option_menu = Menu (my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=test_command)
option_menu.add_command(label="Find next", command=test_command)

# Frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")

root.mainloop()