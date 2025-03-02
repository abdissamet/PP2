with open('file.txt','r') as f, open('file2.txt','a') as s: 
    for i in f:  
             s.write(i)
print("The contents of the file were successfully copied to another file")