#理解递归函数

#后进行先消失
'''
def f1(n):
    print(n)
    if n==0:
        print("over")
    else:
        f1(n-1)
    print("****",n) #见笔记！！！！！！！！！！！！！！解释
f1(4)
'''

#阶乘
def f(n):    #见笔记解释
    if n==1:
        return 1
    else:
        return n*f(n-1)
s=f(4)
print("{0}".format(s))