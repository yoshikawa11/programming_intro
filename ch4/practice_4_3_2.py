# p53指練習
# フィボナッチ数を返す関数を実装する
# fib(5)を求める際にfib(2)の値が計算される回数はいくつか？
# ->fib(2)は7回計算される


def fib(n):
    """n > 0 を整数と仮定
        n 番目のフィボナッチ数を返す """
    if n == 2:                   #追加
        print('fib(n):n=', n)
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))


if __name__ == '__main__':
    print(testFib(5))
