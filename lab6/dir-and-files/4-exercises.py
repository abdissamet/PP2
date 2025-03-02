with open(r"Example ex4.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)