#nonlocal:   声明外部函数的局部变量  与global类似
def outer():
    b=10

    def inner():
        nonlocal b
        print(b)
        b=20   #若要修改，必须先声明
    inner()
    print(b)
outer()