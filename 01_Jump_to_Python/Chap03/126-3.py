# coding: 949
# coffee.py

menu = """
<Menu>
1. Ŀ�� ����
2. Ŀ�� �ܷ� Ȯ��
3. ���α׷� ����
�޴��� �����ϼ��� : """
coffee_number = 10
while True:
    print(menu, end='')
    menu1 = int(input())

    if menu1 == 1:
        money = int(input("�ݾ��� �Է��ϼ��� : "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee_number = coffee_number - 1
        elif money > 300:
            print("Ŀ�Ǹ� �ݴϴ�. ���� �Ž����� %d�Դϴ�." %(money-300))
            coffee_number = coffee_number - 1
        else:
            print("�ݾ��� %d���ڶ��ϴ�." %(300-money))

    if not coffee_number:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break

    elif menu1 == 2:
        print("���� Ŀ���� ���� %d�� �Դϴ�.\n" %coffee_number)
    elif menu1 == 3:
        print("�ǸŸ� �����մϴ�.")
        break
