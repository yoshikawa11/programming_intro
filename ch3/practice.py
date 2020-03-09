# p34指練習
# 2進数10011と等しい10進数
# -> 38

# p37指練習
# ニュートン・ラフソン法と二分法の効率を比較
# ニュートン・ラフソン法:4回 二分法:13回
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

# 平方根を求めるためのニュートン・ラフソン法
# x ** 2 - 25 = 0 で誤差がepsilon 以下になる x を求める
epsilon = 0.01
k = 25.0
guess = k / 2.0
count = 1
while abs(guess * guess - k) >= epsilon:
    print('guess =', guess, 'count =', count)
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    count += 1
print('Square root of', k, 'is about', guess)
