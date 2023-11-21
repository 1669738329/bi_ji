
import copy
#浅拷贝
def Copy():
    a = [10, 20, 30, [5, 6]]
    b = copy.copy(a)
    print("浅拷贝：")
    print("a:", a)
    print("b:", b)

    b.append(40)  # 在b上加40，此时a没有得到40，见笔记
    b[3].append(7)  #因为浅拷贝，在子对象中增加，父类也能得到

    print("a:", a)
    print("b:", b)

#深拷贝
def deepcopy():
    a = [10, 20, 30, [5, 6]]
    b = copy.deepcopy(a)
    print("深拷贝：")
    print("a:", a)
    print("b:", b)

    b.append(40)  #重新创建一个对象，父类一样得不到
    b[3].append(7)  #

    print("a:", a)
    print("b:", b)
Copy()
deepcopy()