# coding: cp949

dish_queue=[]
#dish_queue=['d1','d2','d3','d4']
dish_queue.append('d1')
dish_queue.append('d2')
dish_queue.append('d3')
dish_queue.append('d4')
print("식판 현황: ",end='')
print(dish_queue)

print("{0} 식판 설거지합니다.".format(dish_queue.pop(0)))
print("{0} 식판 설거지합니다.".format(dish_queue.pop(0)))
print("{0} 식판 설거지합니다.".format(dish_queue.pop(0)))
print("{0} 식판 설거지합니다.".format(dish_queue.pop(0)))
