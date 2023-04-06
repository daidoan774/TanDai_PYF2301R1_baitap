import turtle as t

d = t.Screen()
d.bgcolor("black")
rad = 90
m = int(input("input loops: "))
col = ['cyan','blue','pink','purple','yellow','green']
n = 0
i = 0
var = 10
while True:
    t.circle(rad,90)
    t.circle(rad//2,90)
    if n > m:
        break
    else:
        t.color(col[i])
        if i == 5:
            i = 0
        else:
            i+=1
    t.seth(-var)
    t.circle(rad,90)
    t.circle(rad//2,90)
    n+=1
    var+=10
t.speed(1000)         
t.done()