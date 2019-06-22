# import os
# os.getcwd()
# # 'E:\\LearningAfter\\Python'
# os.chdir('E:\LearningAfter\Python\OuterData\chapter3')
# os.getcwd()
# # 'E:\\LearningAfter\\Python\\OuterData\\chapter3'
# data = open('whatsnew.txt')
# print(data.readline(), end='')
# # What's new in 1.63:
# print(data.readline(), end='')
# # -------------------
# data.seek(0)
# # 0
# for each_line in data:
#     print(each_line, end='')
#
# ''' 一长串的内容'''
#
# data.close()
#
# data = open('whatsnew.txt')
# if not each_line.find(':') == -1:
#     (role, line_spoken) = each_line.split(':')
#     print(role, end='')
#     print(' said: ', end='')
#     print(line_spoken, end='')


# data.close()

''' Python 中有两种类型的列表，一种是可以改变的列表（用中括号包围）
    另一种一旦创建就不能改变（用小括号包围），
    后者是一种不可变列表，更常见的称呼是元组（tuple）
    tuple更像一种常量元组
    '''

import os
os.getcwd()
os.chdir('E:\LearningAfter\Python\OuterData\chapter3')
os.getcwd()

# 异常捕获
data = open('sketch.txt')
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    except:
        pass


data.close()