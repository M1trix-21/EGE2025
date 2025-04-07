from turtle import *
tracer (0)
k = 10
for i in range(8):
    fd (16 * k)
    rt(90)
    fd(22 * k)
    rt (90)
up()
fd (5 * k)
rt (90)
fd (5 * k)
lt(90)
down()
for i in range(8):
    fd (52 * k)
    rt (90)
    fd (77 * k)
    rt (90)
up()

for x in range(-50,50):
    for y in range(-50, 50):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update()

