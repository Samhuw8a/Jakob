import yaml

class Settings():
    def __init__(self,path:str,backup_path:str)->None:
        self.path:str = path
        self.backup_path:str = path

    @property
    def settings(self)->dict:
        with open(self.path,"r") as f:
            config = yaml.load(f,Loader=yaml.FullLoader)
        return config

    def write(self,sett:dict)->None:
        with open(self.path,"w") as f:
            config = yaml.dump(sett,f)

class Handler():
    def __init__(self,settings_path:str):
        self.settings_path = settings_path
        self.conf= Settings(settings_path,"Backup.yaml")

    def solve(self,height:float,distance:float)->float:
        return 0.0

    def get_conf(self)->dict:
        return self.conf.settings

    def set_conf(self,sett:dict)->None:
        self.conf.write(sett)

def main()->None:
    h = Handler("Config.yaml")
    c  =h.get_conf()
    print(c)
    c["test"]=False
    h.set_conf(c)
    
if __name__=='__main__':
    main()
