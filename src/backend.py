import yaml

class Settings():
    #TODO:Backup comparison
    def __init__(self,path:str,backup_path:str)->None:
        self.path:str = path
        self.backup_path:str = backup_path

    def is_valid(self,setts:dict)->dict:
        cur:dict = self.backup_settings
        if len(cur)!=len(setts):
            return cur

        for i,j in zip(cur.keys(),setts.keys()):
            if i!=j:
                return cur
        return setts

    @property
    def backup_settings(self)->dict:
        with open(self.backup_path,"r") as f:
            config = yaml.load(f,Loader=yaml.FullLoader)
        return config

    @property
    def settings(self)->dict:
        with open(self.path,"r") as f:
            config = yaml.load(f,Loader=yaml.FullLoader)
        return self.is_valid(config)

    def write(self,sett:dict)->None:
        if self.is_valid(sett) == sett:
            with open(self.backup_path,"w") as f:
               yaml.dump(sett,f)

        with open(self.path,"w") as f:
           yaml.dump(sett,f)
            

class Handler():
    def __init__(self,settings_path:str,backup_path:str):
        self.settings_path = settings_path
        self.conf= Settings(settings_path,backup_path)

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
