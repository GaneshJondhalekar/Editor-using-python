from tkinter import *
from tkinter import filedialog
class Editor:
    def open(self):
        result=filedialog.askopenfile(initialdir="/",title="Open files",filetypes=(("text file",".txt"),("All files","*.*")))
        for i in result:
            self.text.insert(INSERT,i)
    def save_as(self):
        self.s=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if self.s is None:
            return
        self.temp = "True"
        t=self.text.get(1.0,END)
        for i in t:
            self.s.write(i)

    def save(self):
        if self.temp=="True":
            self.s.clear()
            t = self.text.get(1.0, END)
            for i in t:
                self.s.write(i)
        else:
            self.save_as()

    def copy(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def cut(self):
        self.copy()
        self.text.delete("sel.first","sel.last")

    def paste(self):
        self.text.insert(INSERT,self.text.selection_get(selection='CLIPBOARD'))

    def delete(self):
        self.text.selection_get()
        self.text.delete("sel.first","sel.last")

    def new(self):
        self.text.delete(1.0,END)

    def __init__(self,root):
        self.temp="False"
        root.title("GjEditor")
        root.geometry("600x700")
        self.text=Text()
        self.text.pack(fill=BOTH,expand=1)
        self.main_menu=Menu()
        root.config(menu=self.main_menu)

        #creating file menu
        self.file_menu=Menu(tearoff=False)
        self.main_menu.add_cascade(menu=self.file_menu,label="File")
        #creating submenus
        self.new_menu=Menu()
        self.file_menu.add_command(label="New",command=self.new)
        self.open_menu=Menu()
        self.file_menu.add_command(command=self.open,label="Open")
        self.file_menu.add_separator()
        self.save_menu=Menu()
        self.file_menu.add_command(label="Save",command=self.save)
        self.saveas_menu = Menu()
        self.file_menu.add_command(command=self.save_as, label="Save As")
        self.file_menu.add_separator()
        self.exit_menu = Menu()
        self.file_menu.add_command(command=root.destroy, label="Exit")

        #creating edit menu
        self.edit_menu=Menu(tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)
        #creatng submenu
        self.cut_menu = Menu()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.copy_menu = Menu()
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.paste_menu = Menu()
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_separator()
        self.delete_menu = Menu()
        self.edit_menu.add_command(label="Delete", command=self.delete)

        #creating view menu
        self.view_menu=Menu(tearoff=False)
        self.main_menu.add_cascade(menu=self.view_menu,label="View")

        #creating help menu
        self.help_menu=Menu(tearoff=False)
        self.main_menu.add_cascade(menu=self.help_menu,label="Help")

root=Tk()
start=Editor(root)
root.mainloop()
