from tkinter import *
from tkinter.colorchooser import askcolor
import sys

class SettingsWindow(Toplevel):

    def __init__(self,window):
        self.root_window=window
        super().__init__(window)
        self.title("Einstellungen")
        self.get_conf()
        self.make_mess_methode_menu()
        if sys.platform.startswith('win'): 
            self.iconbitmap('Icons/icon.ico')
            
        else:
            logo = PhotoImage(file='Icons/icon.gif')
            self.call('wm', 'iconphoto', self._w, logo)

        self.save_button=Button(self,text="speichern",command=self.set_conf)
        self.save_button.grid(row=2,column=2)

        self.a_entry=Entry(self)
        self.a_entry.grid(row=2,column=1)
        self.b_entry=Entry(self)
        self.b_entry.grid(row=3,column=1)

        self.a_lab=Label(self,text="a:")
        self.a_lab.grid(row=2,column=0)
        self.b_lab=Label(self,text="b:")
        self.b_lab.grid(row=3,column=0)
        
        self.choose_background_but=Button(self,text=" Hintergrund",command=self.choose_background_color,width=15)
        self.choose_background_but.grid(row=1,column=0)
        self.choose_foreground_but=Button(self,text="Schrifftfarbe",command=self.choose_foreground_color,width=15)
        self.choose_foreground_but.grid(row=1,column=1)

        self.get_conf()
        self.set_style()

    def set_conf(self):
        self.new_conf["mess_methode"]=self.aktuell_mess_methode.get()
        try:
            self.new_conf["stab_hoehe"]=float(self.b_entry.get())

        except :
            pass

        try:
            self.new_conf["stab_laenge"]=float(self.a_entry.get())

        except :
            pass
            
        self.root_window.set_config(self.new_conf)
        self.get_conf()
        self.set_style()

    def get_conf(self):
        conf=self.root_window.get_config()
        self.new_conf=conf
        self.bg=conf["backgroud_colour"]
        self.fg=conf["foregroud_colour"]
        self.font=(conf["font"],conf["fontsz"])
        self.aktuell_mess_methode=StringVar(self)
        self.aktuell_mess_methode.set(conf["mess_methode"])
        
              

    def set_style(self):
        self.config(bg=self.bg)
        
        self.save_button.config(bg=self.bg,fg=self.fg,font=self.font)
        self.choose_foreground_but.config(bg=self.bg,fg=self.fg,font=self.font)
        self.choose_background_but.config(bg=self.bg,fg=self.fg,font=self.font)
        self.mess_methode_menu.config(bg=self.bg,fg=self.fg,font=self.font)
        self.mess_methode_lab.config(bg=self.bg,fg=self.fg,font=self.font)
        self.a_entry.config(bg=self.bg,fg=self.fg,font=self.font)
        self.b_entry.config(bg=self.bg,fg=self.fg,font=self.font)
        self.a_lab.config(bg=self.bg,fg=self.fg,font=self.font)
        self.b_lab.config(bg=self.bg,fg=self.fg,font=self.font)

    def choose_background_color(self):
        self.new_conf["backgroud_colour"]=askcolor(parent=self)[1]

    def choose_foreground_color(self):
        self.new_conf["foregroud_colour"]=askcolor(parent=self)[1]
        
    def make_mess_methode_menu(self):
        self.mess_methode_lab=Label(self,text="Mess Methode:")
        self.mess_methode_lab.grid(row=0,column=0)
        self.mess_methode_menu=OptionMenu(self,self.aktuell_mess_methode,"Apian","Strahlensatz",command=self.change_mess_methode)
        self.mess_methode_menu.config(width=12)
        self.mess_methode_menu.grid(row=0,column=1)

    def change_mess_methode(self,choice):
        self.aktuell_mess_methode.set(choice)

class Window(Tk):

    def __init__(self,backend_handler):
        super().__init__()
        self.backend_handler=backend_handler
        self.title("Jakobsstab")
        _=self.get_config()
        self.make_menu()
        self.make_entry_frame()
        if sys.platform.startswith('win'): 
            self.iconbitmap('Icons/icon.ico')
            
        else:
            logo = PhotoImage(file='Icons/icon.gif')
            self.call('wm', 'iconphoto', self._w, logo)
        
    
        self.result_lab=Label(self)
        self.result_lab.grid(row=1,column=1)
        


        self.Image=Label(self)
        
        self.Image.grid(row=0,column=1)
        
        
        self.set_style()
        

    def make_menu(self):
        self.menu=Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Einstellungen",command=self.open_settings_window)
      
    def make_entry_frame(self):
        self.entry_frame=Frame(self)
        self.entry_frame.grid(row=0,column=0)
        self.ha_lab=Label(self.entry_frame,text="ha:")
        
        self.s_lab=Label(self.entry_frame,text=" s:")
        self.ha_entry=Entry(self.entry_frame,width=12)
        self.s_entry=Entry(self.entry_frame,width=12)
        
                
        self.ha_lab.grid(row=1,column=0)
        self.ha_entry.grid(row=1,column=1)   
        self.s_entry.grid(row=0,column=1)
        self.s_lab.grid(row=0,column=0)
        
        
        self.calculate_but=Button(self.entry_frame,text="Ausrechenen",command=self.calculate)
        self.calculate_but.grid(row=2,column=1)

        

    def calculate(self):
        try:
            ha=float(self.ha_entry.get())
            s=float(self.s_entry.get())
            res=round(self.backend_handler.solve(ha,s),2)
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
        image=PhotoImage(file=f"Icons/{self.mess_methode}.gif")
        
        self.Image.config(image=image)
        
        self.mainloop()

        

    def get_config(self):
        conf=self.backend_handler.get_conf()
        self.bg=conf["backgroud_colour"]
        self.fg=conf["foregroud_colour"]
        self.font=(conf["font"],conf["fontsz"])
        self.mess_methode=conf["mess_methode"]
        return conf

    def open_settings_window(self):
        settings_window=SettingsWindow(self)
        settings_window.mainloop()

    def set_config(self,conf):
        self.backend_handler.set_conf(conf)
        _=self.get_config()
        self.make_entry_frame()
        self.set_style()
    

def main():
    from backend import Handler
    window=Window(Handler("src/Config.yaml","src/Backup.yaml"))
    

if __name__ == '__main__':
    main()