str=input("enter a string")
occurns=dict()
words=str.split()
for i in words:
 if i in occurns:
   occurns[i]+=1
 else:
   occurns[i]=1
print("The occurence of eac word is:\n",occurns)
