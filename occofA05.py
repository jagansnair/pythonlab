first=[]
len=int(input("HOW MANY NAMES :"))
for i in range(0,len):
    fname=input("enter the name")
    first.append(fname)
    count_a=0
for names in first:
    count_a+= names.count("a")
print(count_a)
