import yaml
import math

class Settings():
    def __init__(self,path:str,backup_path:str)->None:
        self.path:str = path
        self.backup_path:str = backup_path

    def ret_valid(self,setts:dict)->dict:
        cur:dict = self.backup_settings
        if cur.keys()!=setts.keys():
            return cur
        return setts

    def read_conf(self,path:str)->dict:
        with open(path,"r") as f:
            config = yaml.load(f,Loader=yaml.FullLoader)
        return config

    @property
    def backup_settings(self)->dict:
        return self.read_conf(self.backup_path)

    @property
    def settings(self)->dict:
        res = self.read_conf(self.path)
        return self.ret_valid(res)

    def write(self,sett:dict)->None:
        if self.ret_valid(sett) == sett:
            with open(self.backup_path,"w") as f:
               yaml.dump(sett,f)

        with open(self.path,"w") as f:
           yaml.dump(sett,f)

class Handler():
    def __init__(self,settings_path:str,backup_path:str)->None:
        self.settings_path = settings_path
        self.conf = Settings(settings_path,backup_path)

    def solve_Apian(self,height:float,distance:float,a:float,b:float)->float:
        return height +distance*math.tan(
            2 * math.atan(b/(2*a))
            + math.atan(distance/(height)
            -90))
        #  return ((distance*b)/a)

    def solve_Strahlen(self,height:float,distance:float,a:float,b:float)->float:
        return height+(
            (distance*b)/
            (2*a)
        )

    def solve(self,height:float,distance:float)->float:
        c = self.conf.settings
        a = c["stab_laenge"]
        b = c["stab_hoehe"]

        if c["mess_methode"] == "Apian":
            return self.solve_Apian(height,distance,a,b)
        else:
            return self.solve_Strahlen(height,distance,a,b)

    def get_conf(self)->dict:
        return self.conf.settings

    def set_conf(self,sett:dict)->None:
        self.conf.write(sett)

def main()->None:
    h = Handler("Config.yaml","Backup.yaml")
    c = h.get_conf()
    print(c)
    h.set_conf(c)
    
if __name__=='__main__':
    main()
