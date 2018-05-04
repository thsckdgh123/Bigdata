#coding: 949

print("마름모 출력 프로그램 1.0")

while True:
    num = int(input("밑변 홀수를 입력하세요(0:종료) : "))
    j = num//2
    i = 1
    if num == 0:
        print("프로그램을 종료합니다.")
        break
    elif num%2 == 0:
        print("짝수를 입력하셨습니다. 다시 입력해주세요.")
    else:
        print("  " + "-"*num)
        while i <= num:
            print("ㅣ" + " "*j + "*"*i + " "*j + "ㅣ")
            i += 2
            j -= 1
        j = num-2
        i = 1
        while i <= num//2:
            print("ㅣ" + " "*i + "*"*j + " "*i + "ㅣ")
            i += 1
            j -= 2
        print("  " + "-"*num)
