# p150 指練習
# 再帰による二分探索
# A.(mid+1である理由)mにした場合リストの長さが2の場合無限ループに陥る

def search(L, e):
    """ Lを、要素が昇順で並んだリストとする
        eがLにあればTrueを、そうでなければFalaseを返す"""

    def bSearch(L, e, low, high):
        # high-lowを減少させる
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # 探索対象は残っていない
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
