ch = int(input("nhap chieu cao: "))
cn = int(input("nhap can nang: "))

BMI = round(cn/(ch**2),1)
print("ban co chieu cao la {} m".format(ch))
print("ban co can nang la {} kg".format(cn))

if BMI < 16:
    print("Gầy cấp độ III") 
elif BMI >= 16 and BMI < 17:
    print("Gầy cấp độ II")
elif BMI >= 17 and BMI <18.5:
    print("Gầy cấp độ I")
elif BMI >= 18.5 and BMI < 25:
    print("Bình thường")
elif BMI >=25 and BMI < 30:
    print("Thừa cân")
elif BMI >=30 and BMI < 35:
    print("Béo phì cấp độ I")
elif BMI >=35 and BMI <40:
    print("Béo phì cấp độ II")
else:
    print(" Béo phì cấp độ III")