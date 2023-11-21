def test01():
    print("qweqwe")

test01()
c=test01    #将test01的值（也就是函数的ID），拷贝给c
c()
print(id(test01))
print(id(c))  #id相同