for x in (10,20,30):
    print(x*3,end='\t')
print()
for x in "abcdefg":
    print(x,end='\t')
print()
s={"name":"guo","age":"18","job":"students"}
for x in s:
    print(x,end=' ')
print()
for y in s.values():
    print(y,end=' ')
print()
for z in s.keys():
    print(z,end=' ')
print()
for q in s.items():
    print(q,end=' ')