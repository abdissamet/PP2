import os

def check_path(path):
     if not os.path.exists(path):
        return "The path does not exist"
    
     if not os.access(path, os.R_OK):
         return "Not readable"
     
     if not os.access(path, os.W_OK):
         return "Not writeable"
     
     if not os.path.isdir(path) and os.access(path, os.X_OK):
         return "Non-executable file at the specified path"
     
     return "Access verified successfully."
   
results= check_path("C:/Users/Baseke/Desktop/pp2")
print(results)