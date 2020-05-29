# ハッシュ表
import random


class intDict(object):
    """整数をキーとする辞書"""

    def __init__(self, numBuckets):
        """空の辞書を生成"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, key, dictVal):
        """keyをint型とし，エントリを追加する."""
        hashBucket = self.buckets[key % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))

    def getValue(self, key):
        """keyをint型とする.
           キーkeyに関連付けられた値を返す．"""
        hashBucket = self.buckets[key % self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'  # result[:-1]により最後のカンマを省略


D = intDict(17)
for i in range(20):
    #0 から 10**5 - 1までの整数をランダムに選ぶ
    key = random.choice(range(10**5))
    D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets: #抽象化の壁を侵す
    print('  ', hashBucket)