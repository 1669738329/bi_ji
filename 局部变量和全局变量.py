#全局和局部变量
'''
a=3
print(a)
def add():
    b=4
    print(b*4)
    global a  #改变全局变量
    a=300
    print(a)
    return(b,a)
s=add()
print("a由全局变量变为局部变量:{0}".format(s))
print(globals())  #打印全部的  全局变量
print(locals())   #打印全部的   局部变量
'''


#效率测试
import time
import math

def test01():
    t1 = time.time()
    for i in range(10000000):
        math.sqrt(20)
    t2 = time.time()
    print("耗时:{0}".format(t2-t1))

def test02():
    b=math.sqrt
    t3 = time.time()
    for i in range(10000000):
        b(20)
    t4=time.time()
    print("耗时:{0}".format(t4-t3))

test01()
test02()
