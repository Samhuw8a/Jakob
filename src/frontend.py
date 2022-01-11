from tkinter import *



class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title("Jakobsstab")
        self.get_config()
        self.make_menu()
        self.make_entry_frame()
        
        self.calculate_but=Button(self,text="Ausrechenen",command=self.calculate,font=self.font)
        self.calculate_but.grid(row=1,column=0)
        self.result_lab=Label(self,font=self.font)
        self.result_lab.grid(row=1,column=1)

    def make_menu(self):
        self.menu=Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Einstellungen")
      
    def make_entry_frame(self):
        self.entry_frame=Frame(self)
        self.entry_frame.grid(row=0,column=0)
        
        for name,row in zip(["ha","s"],range(0,2)):
            Label(self.entry_frame,text=name,font=self.font).grid(row=row,column=0)

        self.ha_entry=Entry(self.entry_frame,font=self.font)
        self.s_entry=Entry(self.entry_frame,font=self.font)
        self.s_entry.grid(row=0,column=1)
        self.ha_entry.grid(row=1,column=1)

    def calculate(self):
        self.result_lab.config(text="hallo")

    def get_config(self):
        #add get data from backend

        self.bg="#FFFFFF"
        self.fg="#000000"
        self.font=("Arial",12)
        




def main():
    window=Window()
    window.mainloop()

if __name__ == '__main__':
    main()