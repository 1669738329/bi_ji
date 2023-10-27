#实际参数和形势参数
def printMax(a,b):  #此时  a,b为形式参数
    '''这一般为函数功能介绍'''
    if a>b:
        min=b
        max=a
    else:
        min=a
        max=b
    return max
    print("这一条不执行")   #1.return 语句具有结束函数执行的功能。2.返回值
c=printMax(10,20)  #10,20位实际参数
print("最大值为:{0}".format(c))

def add(x,y,z):
    return [x*10,y*100,z*1000]  #利用元组，字典，列表就可以返回多个数值

s=add(10,20,30)
print("return也可以返回多个数值：{0}".format(s))

help(printMax.__doc__)    #打印此函数的文档注释，注意是双下划线

def azz(x,y):
    s=x+y
    return
q=azz(10,20)
print("若return返回值为空，则返回:{0}".format(q),end=' ')