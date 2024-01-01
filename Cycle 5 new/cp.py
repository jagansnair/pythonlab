

with open("f1.txt", 'r') as f1:
   
    lines = f1.readlines()


with open("f2.txt", 'w') as f2:
    
    f2.writelines(line.strip() + '\n' for line in lines[::2])


with open("f2.txt", 'r') as f3:
    
    contents = [line.strip() for line in f3.readlines()]
    print(contents)
