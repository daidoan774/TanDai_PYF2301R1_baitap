from random import randint

computer_choice = randint(1,3)
current_number = 0
current_player = randint(0, 1)
mas = [1,2,3]
player_choice = " " 
print("Nhập con số bạn muốn 1 - 2 -3: Ai tới 21 trước người đó thua")

while True:
    if current_player == 0 and current_number >= 21:
        print("Bạn thua rồi")
        current_player = 0
        break
    if current_player == 1 and current_number >= 21:
        print("Bạn thắng rồi đó")
        print("Bạn có muốn chơi lại chứ ???")
        play_again = input("")
        if play_again != "y":
               break
        else:
            current_player = 1
            continue  
    else:
        print("Tổng số hiện tại là",current_number) 
        current_number =current_number + computer_choice 
        if current_player == 1:
            print("lượt của máy")
            print("Máy chọn : ", computer_choice)
        else:
            player_choice = input("Số bạn chọn: ")
            print("Máy chọn : ", computer_choice)
            if player_choice in ["1","2","3"]:
                f = int(player_choice)
                for i in mas:
                    x1 = int(mas[0])
                    x2 = int(mas[1])
                    x3 = int(mas[2])
                if f == mas[0]:
                    current_number += x1
                elif f == mas[1]:
                    current_number += x2
                else:
                    current_number += x3
            else:
                print("Bạn phải chọn 1 -2- 3 chứ")
                print("Bạn có muốn chơi lại chứ ???")
                play_again = input("")
                if play_again == "y":
                    continue
                else:
                    break
        

        
      
        
        