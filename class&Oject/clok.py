import turtle
import datetime

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def draw_clock_face(self, pen):
        # Xóa vị trí cũ của kim đồng hồ
       

        # Vẽ mặt đồng hồ và các vạch chia
        pen.penup()
        pen.goto(0, -200)
        pen.pendown()
        pen.circle(200)

        pen.penup()
        pen.goto(0, 0)
        for i in range(12):
            pen.fd(170)
            pen.pendown()
            pen.fd(20)
            pen.penup()
            pen.goto(0, 0)
            pen.rt(30)
    def draw_hands(self, pen):
        # Vẽ kim giờ, kim phút và kim giây
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(90)
        angle = (self.hour / 12) * 360 + (self.minute / 60) * 30
        pen.rt(angle)
        pen.pendown()
        pen.fd(100)

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(90)
        angle = (self.minute / 60) * 360 + (self.second / 60) * 6
        pen.rt(angle)
        pen.pendown()
        pen.fd(150)

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(90)
        angle = (self.second / 60) * 360
        pen.rt(angle)
        pen.pendown()
        pen.fd(180)

        # Cập nhật màn hình
        turtle.update()

    def move_hands(self):
        # Cập nhật giá trị thời gian và di chuyển kim đồng hồ
        now = datetime.datetime.now()
        self.hour = now.hour % 12
        self.minute = now.minute
        self.second = now.second
        turtle.tracer(False)
        pen = turtle.Turtle()
        pen.speed(0)
        self.draw_clock_face(pen)
        self.draw_hands(pen)
        turtle.ontimer(self.move_hands, 1000)
        turtle.clear()

# Tạo một đối tượng đồng hồ và chạy chương trình
clock = Clock(0, 0, 0)
clock.move_hands()
turtle.mainloop()
