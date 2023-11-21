#while循环
num=0
while num<10:
    print(num,end='\t')
    num+=1
num1,sum=0,0
while num1<=100:
    sum+=num1
    num1+=1
print()
print("和为:{0}".format(sum))