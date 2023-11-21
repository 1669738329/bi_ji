import time

start=time.time()
for i in range(1000):
    result=[]
    for m in range(10000):
        result.append(i*1000+m*100)
end=time.time()
print("优化前耗时：{0}".format(end-start))

start2=time.time()
for i in range(1000):
    result=[]
    c=i*1000    #嵌套循环中，尽量减少内层循环的计算，尽可能往外提
    for m in range(10000):
        result.append(c+m*100)
end2=time.time()
print("优化后耗时:{0}".format(end2-start2))