from turtle import *
tracer (0)
k = 7

for i in range(2):
    fd(28 * k)
    rt(90)
    fd(12*k)
    rt(90)
fd(7 * k)
lt (90)
fd (13 * k)
rt (90)
for i in range(2):
    fd(10 * k)
    rt (90)
    fd (30 * k)
    rt (90)
up()

for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update()
