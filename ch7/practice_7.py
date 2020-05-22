# p98指練習
# try-exeptブロックを用いて、下の仕様にあった関数を実装する

def sumDigits(s):
    """sを文字列とする
        sの中の文字の数字の合計を返す。
        例えばsが'a2b3c'ならば5を返す。"""
    count = 0
    for target in s:
        try:
            val = int(target)
            count += val
        except ValueError:
            pass

    return count


if __name__ == '__main__':
    print(sumDigits('a2b3c'))
    print(sumDigits('abc'))


