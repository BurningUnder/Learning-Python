"""
用for循环实现1~100求和
range(i,j)函数提供数值序列i.....j-1
range函数的参数有start, stop, step 数值序列由start开始，到stop-1结束，默认步长step为1
"""

# sum = 0
# for x in range(101):
#     sum+=x
# print(sum)

"""
用for循环实现1~100之间的偶数求和
"""
# sum = 0
# for x in range(2,101,2):
#     sum+=x
# print(sum)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# from random import randint
# num = randint(1,100)
# while True:
#     answer = int(input('请输入一个1~100之间的数值'))
#     if answer < num:
#         print('大一点')
#     elif answer > num:
#         print('小一点')
#     else:
#         print('猜对了')
#         break

"""
输出乘法口诀表(九九表)
print函数的默认结尾是新起一行
"""
# for i in range (1,10):
#     for j in range (1, i+1):
#         print('%d*%d=%d' % (i, j, i*j), end='\t') 
#     print()

"""
输入一个正整数判断它是不是素数
 2 ~  根号m之间的每一个整数去除就可以了
"""
# import math
# while True:
#     num = int(input('请输入一个正整数'))
#     if num > 0:
#         break

# is_Prime = True
# while is_Prime:
#     for i in range (2, int(math.sqrt(num))+1):
#         if num % i ==0:
#             is_Prime = False
#             break
# if is_Prime:
#     print('它是素数')
# else:
#     print('它不是素数')


"""
输入两个正整数计算最大公约数和最小公倍数
最大公约数
    辗转相除法：
        求两个数的最大公约数时，先用较大数除以较小数，如果能整除，最大公约数就等于较小数；
        否则用较小数除以第一步的余数，如果能整除，最大公约数就等于第一步的余数；
        否则，用当前获得的余数除以上一步的余数，直到能整除为止。
        此时作为除数的那个数就是最开始那两个数的最大公约数。
    更相减损法：
        第一步：任意给定两个正整数；判断它们是否都是偶数。若是，则用2约简；若不是则执行第二步。
        第二步：以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。继续这个操作，直到所得的减数和差相等为止。
        用第一步中约掉的若干个2与第二步中等数的乘积就是所求的最大公约数。
最小公倍数
    两个数的最小公倍数等于这两个数的乘积除以这两个数的最大公约数
    求多个数的最小公倍数时，可以先求出其中两个数的最小公倍数，
    再求这两个数的最小公倍数与第三个数的最小公倍数，
    以此类推，直到最后一个数为止。最后得到的最小公倍数就是这几个数的最小公倍数。
"""

# x = int(input('x = '))
# y = int(input('y = '))
# #x为较大的那一个
# if x < y:
#     x, y = y, x

# loss = y
# mul = x * y
# while loss != 0:
#     loss = x % y
#     if loss == 0:
#         print('最大公约数为:%d' % y)
#     else:
#         x = y
#         y = loss
# print('最小公倍数为:%d' % (mul / y))

"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

x = int(input('请输入三角形的高'))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# print()

#用矩阵的想法来解决，就不用去纠结到底要用多少个循环来分别处理空格和星号
# for i in range(1,x+1):
#     for j in range (1,x+1):
#         if i + j <= x:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()    

print()
count = x
for i in range(1,x+1):
    for j in range(1,2*x):
        if i + j <= x or j  >= x + i :
            print('*',end='')
        else:
            print(' ',end='')
    print()
# count = count + 1
    