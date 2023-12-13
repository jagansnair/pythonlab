f_obj = open("para.txt", "r")
lines = f_obj.readlines()
l1 = [line.strip() for line in lines]
print("Lines read using readlines():")
print(lines)
print("\nLines stored in a list after stripping:")
print(l1)
print("\nLines using list comprehension while opening the file:")
print([line.strip() for line in open('para.txt', 'r')])
