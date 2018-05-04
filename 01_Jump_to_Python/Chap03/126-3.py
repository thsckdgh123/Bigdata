# coding: 949
# coffee.py

menu = """
<Menu>
1. 커피 구매
2. 커피 잔량 확인
3. 프로그램 종료
메뉴를 선택하세요 : """
coffee_number = 10
while True:
    print(menu, end='')
    menu1 = int(input())

    if menu1 == 1:
        money = int(input("금액을 입력하세요 : "))
        if money == 300:
            print("커피를 줍니다.")
            coffee_number = coffee_number - 1
        elif money > 300:
            print("커피를 줍니다. 여기 거스름돈 %d입니다." %(money-300))
            coffee_number = coffee_number - 1
        else:
            print("금액이 %d모자랍니다." %(300-money))

    if not coffee_number:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

    elif menu1 == 2:
        print("남은 커피의 양은 %d개 입니다.\n" %coffee_number)
    elif menu1 == 3:
        print("판매를 종료합니다.")
        break
