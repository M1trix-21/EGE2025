from turtle import *
tracer (0)
k = 7

for i in range(9):
    fd(12 * k)
    rt(90)
    fd(6*k)
    rt(90)
up()
fd(1 * k)
rt (90)
fd (3 * k)
lt (90)
down()
for i in range(9):
    fd(53 * k)
    rt (90)
    fd (75 * k)
    rt (90)
up()

for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update()