import turtle  #导入模块
t=turtle.Pen()  #注意画笔“Pen”是大写
t.speed(5)    #画笔速度，越大越快，最大为0
'''
t.goto(0, 0)
#循环画法
my_colors=("red","black","blue","yellow","green")  #画笔颜色，记得加引号
for i in range(10):
    t.penup()
    t.goto(0,-i*50)
    t.pendown()
    t.width(20)
    t.color(my_colors[i%len(my_colors)])
    t.circle(50+i*50)
turtle.done()
'''

#普通画法，把注释删了看
'''
t.circle(100)  #逆时针画圆,且起点是在底部  在Pycharm中
t.penup() #抬起画笔
t.goto(0,-50)  #移动到指定坐标
t.pendown()   #落笔
t.circle(150)
t.penup()
t.goto(0,-100)
t.pendown()
t.circle(200)
turtle.done()  #程序执行完，窗口依然在
'''
#棋盘画法
for y in range(19):   #画横线
    t.penup()
    t.goto(-300,300-y*30)
    t.pendown()
    t.goto(240,300-y*30)
for x in range(19):   #画竖线
    t.penup()
    t.goto(-300+x*30,300)
    t.pendown()
    t.goto(-300+x*30,-240)

for x in range(3):    #星位
    x=300-2-90-x*180
    for i in range(3):
        t.penup()
        t.goto(-300+90+i*180,x)
        t.pendown()
        t.width(3)
        t.circle(2)
turtle.done()

#星位废稿

'''for i in range(1,10):
    x=0
    t.penup()
    t.goto(-300+90*i,300-90-2)
    t.pendown()
    t.circle(2)
    if i%3==0:
        x=x+1
        i=i-2
        t.penup()
        t.goto(-300+90*i,300-90*x-2)
        t.pendown()
        t.circle(2)
        '''
