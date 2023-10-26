#多分支结构
score=int(input("请输入成绩:"))
grade=""

if score<60:
    garde="不及格"
elif score<80:
    garde="及格"
else:
    garde="优秀"
print("分数是{0}，等级是{1}".format(score,garde))