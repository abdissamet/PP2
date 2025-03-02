lst = ['BMW', 'Rolls Royse', 'Mercedes']
with open('file.txt', 'w+') as f:
    for i in lst:
        f.write('%s\n' %i)
    print("File written successfull")
f.close()