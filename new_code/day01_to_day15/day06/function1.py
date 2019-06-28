"""
实现计算求最大公约数和最小公倍数的函数
"""

def gcd(x, y):
    if x < y:
        x, y = y,x
    for factor in range(y, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

# x = int(input('x = '))
# y = int(input('y = '))

# print(gcd(x,y))
# print(lcm(x,y))
"""
实现判断一个数是不是回文数的函数
"""
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

"""
说实话这个我是真没想出来这么好的解决方法
我想到可以求余数然后对比，但是没想出保存余数的方法
因为没想到怎么知道数的位数
但是这个解答是可以不用考虑数的位数
这个*10+余数真的挺好的，比我的效率高的多
"""

"""
判断一个数是不是素数
1既不是素数也不是合数
"""
from math import sqrt
def is_Prime(num):
    for factor in range(2, int(sqrt(num))+1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

"""
写一个程序判断输入的正整数是不是回文素数
"""

if __name__ == "__main__":
    num = int(input('num = '))
    if is_Prime(num):
        if is_palindrome(num):
            print('是回文素数')
    else:
        print('不是回文素数')
