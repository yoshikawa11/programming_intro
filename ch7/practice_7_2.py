# p101指練習
# 次の仕様にあった関数を実装する

def findAnEven(L):
    """ Lをint型の要素をもつリストとする
        Lに最初に現れる偶数を返す
        Lが偶数を含まなければValueErrorを引き起こす"""
    for target in L:
        if target % 2 == 0:
            return target
    raise ValueError


if __name__ == '__main__':
    print(findAnEven([1, 2, 3, 4, 5]))
    try:
        print(findAnEven([1, 3, 5]))
    except ValueError:
        print('ValueError happened')
