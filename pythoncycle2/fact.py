def fact(num):
    f=1
    if num==0:
       print("Factorial is:",f)
    elif num<0:
        print("Can't find the factorial")
    else:
        for i in range(1,num+1):
         f=f*i
        print("Factorial of",num,"is",f)
num=int(input("Enter the number to find factorial"))
fact(num)               
