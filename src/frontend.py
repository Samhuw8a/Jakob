from tkinter import *

class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title("Jakobsstab")
        self.geometry("300x100")
        self.make_menu()
        self.make_entry_frame()

    def make_menu(self):
        self.menu=Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Einstellungen")

    def make_entry_frame(self):
        self.entry_frame=Frame(self)
        self.entry_frame.grid(row=0,column=0)
        
        for name,row in zip(["a","b","ha","s"],range(0,4)):
            Label(self.entry_frame,text=name).grid(row=row,column=0)

        self.a_entry=Entry(self.entry_frame)
        self.b_entry=Entry(self.entry_frame)
        self.ha_entry=Entry(self.entry_frame)
        self.s_entry=Entry(self.entry_frame)

        self.a_entry.grid(row=0,column=1)
        self.b_entry.grid(row=1,column=1)
        self.s_entry.grid(row=2,column=1)
        self.ha_entry.grid(row=3,column=1)
        
def main():
    window=Window()
    window.mainloop()

if __name__ == '__main__':
    main()