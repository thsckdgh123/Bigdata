#coding: 949

print("������ ��� ���α׷� 1.0")

while True:
    num = int(input("�غ� Ȧ���� �Է��ϼ���(0:����) : "))
    j = num//2
    i = 1
    if num == 0:
        print("���α׷��� �����մϴ�.")
        break
    elif num%2 == 0:
        print("¦���� �Է��ϼ̽��ϴ�. �ٽ� �Է����ּ���.")
    else:
        while i <= num:
            print(" "*j + "*"*i)
            i += 2
            j -= 1
