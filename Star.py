import simplegui
import random
a= random.randint(225,380)
b= random.randint(225,380)
c= random.randint(225,380)
d= random.randint(225,380)
e= random.randint(285,380)
f= random.randint(285,380)
g= random.randint(285,380)
h= random.randint(285,380)
i= random.randint(285,380)
j= random.randint(285,380)
k= random.randint(225,380)
l= random.randint(225,380)

x = 150
def draw_handler(canvas):
    global x
    x = x + 10
    if(x >= 600):
        x = 50
    canvas.draw_polygon([(0,0),(600,0),(600,600),(0,600)], 50, "Green")
    canvas.draw_polygon([(50,50),(550,50),(550,550),(50,550)], 50, "Red")
    canvas.draw_polygon([(100,100),(500,100),(500,500),(100,500)], 50, "Green")
    canvas.draw_polygon([(150,150),(450,150),(450,450),(150,450)], 50, "Red")
    canvas.draw_polygon([(200,200),(400,200),(400,400),(200,400)], 50, "Green")
    canvas.draw_polygon([(250,250),(350,250),(350,350),(250,350)], 50, "Red", "White")
    canvas.draw_circle((x, 50), 70, 20, "White", "Gold")
    canvas.draw_circle((x, 150), 70, 20, "Gold", "White")
    canvas.draw_circle((x, 250), 70, 20, "White", "Gold")
    canvas.draw_circle((x, 350), 70, 20, "Gold", "White")
    canvas.draw_circle((x, 450), 70, 20, "White", "Gold")
    canvas.draw_circle((x, 550), 70, 20, "White", "Gold")
    canvas.draw_line((300,0), (175,300), 20, "Black")
    canvas.draw_line((185,300), (0,300), 20, "Black")
    canvas.draw_line((300,0), (425,300), 20, "Black")
    canvas.draw_line((415,300), (600,300), 20, "Black")
    canvas.draw_line((0,300), (185,410), 20, "Black")
    canvas.draw_line((600,300), (415,410), 20, "Black")
    canvas.draw_line((415,440), (415,600), 20, "Black")
    canvas.draw_line((415,300), (600,300), 20, "Black")
    canvas.draw_line((415,300), (600,300), 20, "Black")  
    canvas.draw_line((415,400), (415,600), 20, "Black")
    canvas.draw_line((185,400), (185,600), 20, "Black")
    canvas.draw_line((185,600), (310,400), 20, "Black")
    canvas.draw_line((415,600), (290,400), 20, "Black")
    canvas.draw_polygon([(300,0),(185,300),(0,300),(185,410),(185,600),(310,400),(415,600),(415,400),(600,300),(415,300)],40,"Gold","White")
    canvas.draw_circle((a,e),4,1,"red","green")
    canvas.draw_circle((b,f),4,1,"red","green")
    canvas.draw_circle((c,g),4,1,"red","green")
    canvas.draw_circle((d,h),4,1,"red","green")
    canvas.draw_circle((l,i),4,1,"red","green")
    canvas.draw_circle((k,j),4,1,"red","green")
    for x in range(300,x):
        canvas.draw_polygon([(0,0),(600,0),(600,600),(0,600)], 50, "Red")
        canvas.draw_polygon([(50,50),(550,50),(550,550),(50,550)], 50, "Green")
        canvas.draw_polygon([(100,100),(500,100),(500,500),(100,500)], 50, "Red")
        canvas.draw_polygon([(150,150),(450,150),(450,450),(150,450)], 50, "Green")
        canvas.draw_polygon([(200,200),(400,200),(400,400),(200,400)], 50, "Red")
        canvas.draw_polygon([(250,250),(350,250),(350,350),(250,350)], 50, "Green", "White")
        x = x + 10
        if(x >= 600):
            x = 50

    for x in range(225,x):
        canvas.draw_polygon([(300,0),(185,300),(0,300),(185,410),(185,600),(310,400),(415,600),(415,400),(600,300),(415,300)],40,"White","Gold")
        canvas.draw_circle((a,e),4,1,"red","green")
        canvas.draw_circle((b,f),4,1,"red","green")
        canvas.draw_circle((c,g),4,1,"red","green")
        canvas.draw_circle((d,h),4,1,"red","green")
        canvas.draw_circle((l,i),4,1,"red","green")
        canvas.draw_circle((k,j),4,1,"red","green")
        x = x + 10
        if(x >= 600):
            x = 50
    canvas.draw_circle((x, 50), 70, 20, "White", "Gold")
    canvas.draw_circle((x, 150), 70, 20, "Gold", "White")
    canvas.draw_circle((x, 250), 70, 20, "White", "Gold")
    canvas.draw_circle((x, 350), 70, 20, "Gold", "White")
    canvas.draw_circle((x, 450), 70, 20, "White", "Gold")
    canvas.draw_circle((x, 550), 70, 20, "White", "Gold")

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
