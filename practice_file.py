#p.18指練習
#x,y,z をリストに格納
list = [14, 30, 7]
list_odd = []
list_count = len(list)
count_even = 0
for i in list:
    if i % 2 == 0:
        count_even += 1
        continue
    else:
        list_odd.append(i)
    continue
if count_even == list_count:
    print("所与の変数に奇数は存在しない")
else:
    print("最も大きい奇数:" + str(list_odd))





