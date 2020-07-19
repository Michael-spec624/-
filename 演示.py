import turtle
import time

#移动画笔到指定位置
def Mov(p,x,y):
    p.up()
    p.goto(x,y)
    p.down()

#在指定位置放置盘子
def MovP(p,x,y,abc):
    p.clear()
    Mov(p,x,y)
    if (abc==1):
        p.forward(60)
    if(abc==2):
        p.forward(40)
    if(abc==3):
        p.forward(20)
    time.sleep(1)

#在画布上移动盘子
def mov():
    MovP(pc,90,-95,3)
    MovP(pb,-20,-95,2)
    MovP(pc,-10,-85,3)
    MovP(pa,70,-95,1)
    MovP(pc,-110,-95,3)
    MovP(pb,80,-85,2)
    MovP(pc,90,-75,3)

#绘制汉诺塔游戏背景图
def bg():
    Mov(p,-200,-100)
    p.forward(400)
    p.setheading(90)
    for i in range(3):
        Mov(p,(i-1)*100,-100)
        p.forward(200)
        p.write(chr(ord('A')+i), font = ('Arial',20,'normal'))
    p.hideturtle()
    MovP(pa,-130,-95,1)
    MovP(pb,-120,-85,2)
    MovP(pc,-110,-75,3)



#设置每只画笔的颜色和尺寸    
def setpen(p,s,i):
    p.pensize(s)
    p.pencolor(pcolor[i])

#主程序

pa=turtle.Pen()
pb=turtle.Pen()
pc=turtle.Pen()
p=turtle.Pen()
pcolor=['blue','red','orange','green']
setpen(p,5,0)
setpen(pa,10,1)
setpen(pb,10,2)
setpen(pc,10,3)
bg()
mov()
turtle.done()