# p41指練習
# ２つの文字列を引数とし、どちらか一方の文字列に他方の文字列が含まれる場合trueを、
# それ以外の場合はfalseを返す関数


def isIn(str1, str2):

    if len(str1) > len(str2):
        str1, str2 = str2, str1
    if str1 in str2:
        return True
    else:
        return False

# 引数の順番が関数の判定に依存しないことを確認する
if __name__ == '__main__':
    print(isIn('testabc', 'test'))
    print(isIn('intro', 'programmingintro'))
