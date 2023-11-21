for x in range(5):
    for y in range (5):
        print(x,end='\t')
    print()

#九九乘法表
for x in range(1,10):
    for y in range(1,10):
        s=x*y
        if x>=y:
            print("{0}*{1}={2}".format(y,x,s),end='\t')
    print()