a = input("input a = ")
x = a.split(" ",1)

print(f"bạn vừa nhập 2 số {x}")
for i in x:
    x1 = int(x[0])
    x2 = int(x[1])
if x2 < x1:
    print("Số kết thúc cần lớn hơn số bắt đầu:")
else:
    for j in range(x1,x2):
        
        if j%3 == 0 and j%5 == 0:
            print(f"Số này là {j} FizzBuzz")
        elif j%3 == 0:
            print(f"Số này là {j} Fizz")
        elif j%5 == 0:
            print(f"Số này là {j} Buzz")
        else:
            print(j)