#列表推导式
y=[x*2 for x in range(1,50) if x%5==0]
print(y)

  #循环生成
y=[]
for x in range(1,50):
    if x%5==0: y.append(x*2)  #  append()是原地修改列表元素，在列表尾部添加新元素，且不产生新对象
print(y)

#可以使用两个循环
s=[(x,y) for x in range(1,10) for y  in range(1,10)]
print(s)

#字典推导式
my_text="i love you,i love sxt,i love python"
char_count={c:my_text.count(c) for c in my_text}
print(char_count)

#集合推导式
s={x for x in range(1,100) if(x%9==0)}
print(s)

#生成器推导式（生成元组）
s=(x for x in range(4))
#print(tuple(x))   #tuple()是构建元组的一种方式
for x in s:  #s是生成器对象，生成器是可迭代的对象
    print(x,end=',')
print()
print(tuple(s),end=' ')