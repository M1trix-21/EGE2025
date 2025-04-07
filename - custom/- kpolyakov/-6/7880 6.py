from turtle import *
tracer (0)
k = 7

for i in range(2):
    fd(24 * k)
    rt(90)
    fd(10*k)
    rt(90)
fd(5 * k)
lt (90)
fd (12 * k)
rt (90)
for i in range(2):
    fd(9 * k)
    rt (90)
    fd (35 * k)
    rt (90)
up()

for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update()