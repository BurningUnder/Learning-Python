import os

os.getcwd()
os.chdir('E:\LearningAfter\Python\OuterData\chapter3')
os.getcwd()

if os.path.exists('whatsnot.txt'):
    print('have find it')
else:
    print("the file is missing")

# 针对不同的异常进行的捕获
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')
        except ValueError:
            # pass就是空子句，什么也不做，python不能直接为空，可能是没有约束的原因
            pass

    data.close()
except IOError:
    print('the data file is missing')
