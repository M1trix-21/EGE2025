from turtle import *
tracer (0)
k = 7

for i in range(2):
    fd(55 * k)
    rt(90)
    fd(22.8*k)
    rt(90)
fd(17.3 * k)
lt (90)
fd (25.4 * k)
rt (90)
for i in range(2):
    fd(15.6 * k)
    rt (90)
    fd (70.8 * k)
    rt (90)
up()

for x in range(-100,100):
    for y in range(-100, 100):
        goto(x * k, y * k )
        dot(3,'green'
            )
done()
update()