import os

def directories(path):
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            print(i)
            return i

def files(path):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            print(i)
            return i

def all(path):
    return os.listdir(path)

specified_path = "C:/Users/Baseke/Desktop/pp2/lab6/dir and files"

print("Directories:")
print(directories(specified_path))

print("\nFiles:")
print(files(specified_path))

print("\nAll Directories and Files:")
print(all(specified_path))