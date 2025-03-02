import string

def create_files():
    al = string.ascii_uppercase
    for i in al:
        file_name = i + ".txt"
        with open(file_name, 'w') as file:
            file.write("This is file " + file_name)
create_files()