import turtle
import colorsys
t=turtle.Turtle()
wn=turtle.Screen()
wn.setup(height=2000,width=1000,startx=0,starty=0)
t.speed(0)
t.pensize(4)
def goto1(x,y):
	t.up()
	t.goto(x,y)
	t.down()

def draw():
	goto1(-100,300)
	t.fillcolor("yellow")
	t.begin_fill()
	t.lt(20)
	t.circle(-300,45)
	t.bk(15)
	t.lt(90)
	t.circle(-200,55)
	t.rt(90)
	t.circle(-200,55)
	t.lt(40)

	for i in range(10):
		t.lt(2)
		t.fd(10)
	for i in range(20):
		t.fd(5)
		t.rt(1.5)
	t.rt(25)
	
	for i in range(70):
		t.fd(6)
		t.rt(1)
	goto1(-100,300)
	t.rt(135)
	t.fd(15)
	t.lt(90)
	t.circle(200,55)
	t.lt(90)
	t.circle(200,55)
	t.rt(40)
	for i in range(10):
		t.rt(2)
		t.fd(10)
	for i in range(25):
		t.fd(5)
		t.lt(1.5)
	t.lt(25)
	t.end_fill()
	t.fillcolor("yellow")
	t.begin_fill()
	for i in range(46):
		t.fd(6)
		t.lt(1)
	t.end_fill()
	goto1(-80,280)
	t.rt(110)
	t.pensize(50)
	t.color("yellow")
	t.fd(260)
	t1=turtle.Turtle()
	t1.pensize(10)
	t1.color("white")
	t1.up()
	t1.goto(50,-77)
	t1.down()
	t1.rt(165)
	for i in range(40):
		t1.fd(6)
		t1.rt(1)
	t1.goto(50,-78)
	t1.color("white")
	t1.lt(25)
	t1.fillcolor("white")
	t1.begin_fill()
	for i in range(40):
		t1.fd(6)
		t1.rt(1)
	t1.lt(90)
	t1.fd(200)
	t1.goto(50,-79)
	t1.end_fill()
	t.pensize(4)
	t.color("black")
	t.fillcolor("black")
	goto1(250,300)
	t.begin_fill()
	t.lt(190)
	for i in range(52):
		t.fd(2)
		t.lt(1)
	t.rt(110)
	for i in range(26):
	    t.fd(2)
	    t.rt(1)
	t.rt(80)
	for i in range(37):
	    t.fd(3)
	    t.rt(1)
	t.end_fill()
	goto1(-220,300)
	t.rt(127)
	t.begin_fill()
	for i in range(40):
		t.fd(3)
		t.rt(1)
	t.rt(80)
	for i in range(18):
		t.fd(3)
		t.rt(1)
	t.rt(115)
	for i in range(57):
		t.fd(2)
		t.lt(1)
	t.end_fill()
	goto1(-130,170)
	t.begin_fill()
	t.circle(35)
	t.end_fill()
	t.fillcolor("white")
	goto1(-105,178)
	t.begin_fill()
	t.circle(15)
	t.end_fill()
	goto1(100,170)
	t.fillcolor("black")
	t.begin_fill()
	t.circle(35)
	t.end_fill()
	goto1(115,178)
	t.fillcolor("white")
	t.begin_fill()
	t.circle(15)
	t.end_fill()
	goto1(-190,40)
	t.fillcolor("red")
	t.begin_fill()
	t.circle(50)
	t.end_fill()
	goto1(118,40)
	t.begin_fill()
	t.circle(50)
	t.end_fill()
	goto1(20,100)
	t.lt(40)
	t.circle(50,80)
	goto1(20,100)
	t.rt(180)
	t.circle(-50,80)
	t.lt(15)
	t.bk(30)
	t.rt(65)
	t.fillcolor("pink")
	t.begin_fill()
	for i in range(25):
		t.lt(1)
		t.bk(3)
	for i in range(40):
		t.lt(3)
		t.bk(1)
	for i in range(27):
		t.lt(1)
		t.bk(3)
	t.rt(70)
	t.circle(-50,54)
	t.lt(83)
	t.circle(-50,57)
	t.end_fill()
	
	goto1(35,120)
	t.rt(170)
	t.fillcolor("black")
	t.ht()
	t.begin_fill()
	for i in range(3):
	    t.lt(120)
	    t.fd(30)
	t.end_fill()
	
draw()
wn.mainloop()