import src.backend as backend
import src.frontend as frontend

def main()->None:
    path="config/"
    handler = backend.Handler(path+"Config.yaml",path+"Backup.yaml")
    gui = frontend.Window(handler)

    

if __name__=='__main__':
    main()
