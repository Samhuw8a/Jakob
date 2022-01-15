import src.backend as backend

def main()->None:
    path="src/"
    handler = backend.Handler(path+"Config.yaml",path+"Backup.yaml")

if __name__=='__main__':
    main()
