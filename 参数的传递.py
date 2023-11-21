#传递可变对象  m  列表，字典：可以修改的是可变对象 append
'''
a=[10,20]

print(id(a))
print(a)
def test(m):
    print(id(m))  #指向同一个对象,将a传给m,操作单位是同一个对象
    m.append(30)
    print(id(m))
    print(a)
test(a)
'''

#浅拷贝和深拷贝

import copy
#浅拷贝
def Copy():
    a = [10, 20, 30, [5, 6]]
    b = copy.copy(a)
    print("浅拷贝：")
    print("a:", a)
    print("b:", b)

    b.append(40)  # 在b上加40，此时a没有得到40，见笔记
    b[3].append(7)  #

    print("a:", a)
    print("b:", b)

#深拷贝
def deepcopy():
    a = [10, 20, 30, [5, 6]]
    b = copy.deepcopy(a)
    print("深拷贝：")
    print("a:", a)
    print("b:", b)

    b.append(40)
    b[3].append(7)  #

    print("a:", a)
    print("b:", b)
Copy()
deepcopy()