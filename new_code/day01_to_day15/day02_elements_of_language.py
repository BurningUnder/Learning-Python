# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# #整除
# print(a // b)
# #模
# print(a % b)
# #指数
# print(a ** b)

"""
    使用input函数输入
    以占位符形式输出
"""
# a = input()
# print(a)
# #或者
# a = int(input('a= '))
# print(a)
# print(type(a))#输入默认保存为字符串类型
#
# print('%d+%d=%d'% (a,a,a+a))

"""
    身份运算符
"""
# a = 10
# b = 10
# print(a is b)
# print('id of a,b: %d,%d' % (id(a),id(b)))
# c = True
# print(c is bool)
# print(id(c))

"""
    华氏温度转摄氏温度
    F = 1.8C+32    
"""
# f = float(input('请输入华氏温度'))
# c = (f - 32) / 1.8
# print('摄氏温度是：',c)

"""
    计算圆的周长和面积
    """
# import math
# r = int(input('请输入半径：'))
# l = 2 * math.pi * r
# area = math.pi * (r ** 2)
# print('length : %f, area : %f' % (l,area))

"""
    计算闰年
    （1）能被4整除但不能被100整除的年份为普通闰年
    （2）能被400整除的为世纪闰年
    """

years = int(input('输入年份'))

if years % 4 == 0 and years % 100 != 0:
    print(years,'年是普通闰年')
elif years % 400 ==0:
        print(years,'年是世纪闰年')
else:
    print(years,'年不是闰年')
