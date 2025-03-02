import os

def analyse(path):
    if os.path.exists(path):
        print("The path exists")
        
        file=os.path.basename(path)
        direc=os.path.dirname(path)
        print(f"filename: {file}")
        print(f"Directory: {direc}")
    else:
        print("The path does not exists")
p=analyse("C:/Users/Baseke/Desktop/pp2/lab6/dir and files")