#p.18指練習
#x,y,z をリストに格納
# list = [14, 30, 7]
# list_odd = []
# list_count = len(list)
# count_even = 0
# for i in list:
#     if i % 2 == 0:
#         count_even += 1
#         continue
#     else:
#         list_odd.append(i)
#     continue
# if count_even == list_count:
#     print("所与の変数に奇数は存在しない")
# else:
#     print("最も大きい奇数:" + str(list_odd))


# p22指練習
# whileループで書き換え
# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ' '
# PrintX = 'X'
# if numXs < 0:
#     numXs = numXs * -1
# while numXs > 0:
#     toPrint += PrintX
#     numXs += -1
# print(toPrint)

# p24指練習
# 10個の整数の入力を促しその中の最大の奇数を表示する
# numXs = (input('Input 10 numbers: '))
# line = numXs.split()
# count = 1
# targetNum = ''
# for i in line:
#     if int(i) % 2 != 0:
#         if targetNum == '':
#             targetNum = i
#         else:
#             if int(targetNum) < int(i):
#                 targetNum = i
# if targetNum == '':
#     print('奇数が存在しない')
# else:
#     print('最大の奇数:' + str(targetNum))

# p27指練習
# 入力値に等しいroot**pwdを求める
numX = int(input('Input 1 number: '))
root = 1
pwr = 1
while pwr < 6:
    if numX == root ** pwr:
        break
    else:
        # if numX < root ** pwr:
        #     pwr += 1
        # else:
        #     root += 1
        pwr += 1
        count = 1
        while numX >= count ** pwr:
            count += 1
            if numX == count ** pwr:
                root = count

if numX == root ** pwr:
    print('Input number: ' + str(numX) + ' root: ' + str(root) + ' pwr: ' + str(pwr))
else:
    print('There is no such pair')
