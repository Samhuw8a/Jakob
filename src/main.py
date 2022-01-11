import backend
#  import frontend

def main()->None:
    path="src/" if 0 else ""
    handler = backend.Handler(path+"Config.yaml",path+"Backup.yaml")
    print(handler.get_conf())

if __name__=='__main__':
    main()
