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
        print("  " + "-"*num)
        while i <= num:
            print("��" + " "*j + "*"*i + " "*j + "��")
            i += 2
            j -= 1
        j = num-2
        i = 1
        while i <= num//2:
            print("��" + " "*i + "*"*j + " "*i + "��")
            i += 1
            j -= 2
        print("  " + "-"*num)
