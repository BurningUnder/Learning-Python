"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

from math import sqrt


for num in range (1,10000):
    sum = 1
    num_sqr = int(sqrt(num))
    #从2 开始循环可以排除自身这个因子
    for i in range (2,num_sqr+1):
        #整除
        if num % i == 0:
            #得到一个因子
            sum += i
            #在这里还要考虑到因子会不会相同例如9*9=81
            if num / i != i:
                sum += num / i
    if sum == num:
        print('%d是完全数' % num)