from tkinter import *
from backend import *
from tkinter.colorchooser import askcolor

class SettingsWindow(Toplevel):

    def __init__(self,window):
        self.root_window=window
        super().__init__(window)
        self.title("Einstellungen")

        self.save_button=Button(self,text="speichern",command=self.set_conf)
        self.save_button.pack()
        
        self.get_conf()
        self.set_style()

    def set_conf(self):
        self.root_window.set_config({'backgroud_colour': '#070707', 'font': 'Arial', 'fontsz': 13, 'foregroud_colour': '#f2d8b8', 'mess_methode': 'Apian', 'stab_hoehe': 5.0, 'stab_laenge': 2.0})
        self.get_conf()
        self.set_style()

    def get_conf(self):
        conf=self.root_window.get_config()
        self.bg=conf["backgroud_colour"]
        self.fg=conf["foregroud_colour"]
        self.font=(conf["font"],conf["fontsz"])

    def set_style(self):
        self.config(bg=self.bg)
        self.save_button.config(bg=self.bg,fg=self.fg,font=self.font)


class Window(Tk):

    def __init__(self,backend_handler):
        super().__init__()
        self.backend_handler=backend_handler
        self.title("Jakobsstab")
        _=self.get_config()
        self.make_menu()
        self.make_entry_frame()
        
        self.calculate_but=Button(self,text="Ausrechenen",command=self.calculate)
        self.calculate_but.grid(row=1,column=0)
        self.result_lab=Label(self)
        self.result_lab.grid(row=1,column=1)
        self.set_style()

    def make_menu(self):
        self.menu=Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Einstellungen",command=self.open_settings_window)
      
    def make_entry_frame(self):
        self.entry_frame=Frame(self)
        self.entry_frame.grid(row=0,column=0)
        
        self.ha_lab=Label(self.entry_frame,text="ha:")
        self.ha_lab.grid(row=1,column=0)
        self.s_lab=Label(self.entry_frame,text=" s:")
        self.s_lab.grid(row=0,column=0)

        self.ha_entry=Entry(self.entry_frame)
        self.s_entry=Entry(self.entry_frame)
        self.s_entry.grid(row=0,column=1)
        self.ha_entry.grid(row=1,column=1)

    def calculate(self):
        try:
            ha=float(self.ha_entry.get())
            s=float(self.s_entry.get())
            res=self.backend_handler.solve(ha,s)
        except:
            res="ERROR"

        self.result_lab.config(text=res)

    def set_style(self):
        self.configure(bg=self.bg)
        self.entry_frame.config(bg=self.bg)
        #add color config of image frame
        self.calculate_but.config(bg=self.bg,fg=self.fg,font=self.font)
        self.result_lab.config(bg=self.bg,fg=self.fg,font=self.font)
        self.ha_entry.config(bg=self.bg,fg=self.fg,font=self.font)
        self.s_entry.config(bg=self.bg,fg=self.fg,font=self.font)
        self.ha_lab.config(bg=self.bg,fg=self.fg,font=self.font)
        self.s_lab.config(bg=self.bg,fg=self.fg,font=self.font)

    def get_config(self):
        conf=self.backend_handler.get_conf()
        self.bg=conf["backgroud_colour"]
        self.fg=conf["foregroud_colour"]
        self.font=(conf["font"],conf["fontsz"])
        return conf

    def open_settings_window(self):
        settings_window=SettingsWindow(self)
        settings_window.mainloop()

    def set_config(self,conf):
        self.backend_handler.set_conf(conf)
        _=self.get_config()
        self.set_style()
    

def main():
    window=Window(Handler("src/Config.yaml","src/Backup.yaml"))
    window.mainloop()

if __name__ == '__main__':
    main()