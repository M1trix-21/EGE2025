from turtle import *
tracer (0)
k = 7

for i in range(3):
    fd(7 * k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(4 * k)
rt (90)
fd (6 * k)
lt (90)
down()
for i in range(4):
    fd(83 * k)
    rt (90)
    fd (77 * k)
    rt (90)
up()

for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update() # tyt