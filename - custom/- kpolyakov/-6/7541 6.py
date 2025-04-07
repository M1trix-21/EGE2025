from turtle import *
tracer (0)
k = 7

for i in range(10):
    fd(22 * k)
    rt(90)
    fd(16*k)
    rt(90)
up()
fd(1 * k)
rt (90)
fd (1 * k)
lt (90)
down()
for i in range(10):
    fd(72 * k)
    rt (90)
    fd (79 * k)
    rt (90)
up()

for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update()