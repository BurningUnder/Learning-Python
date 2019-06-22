import os

os.getcwd()
os.chdir('E:\LearningAfter\Python\OuterData\chapter3')
os.getcwd()

man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)

        except ValueError:
            pass
    data.close()
except IOError:
   print('the datafile is missing')

try:
    out1 = open('man_data.txt', 'w')
    out2 = open('other_data.txt', 'w')
    print(man, file=out1)
    print(other, file=out2)
    out1.close()
    out2.close()
except IOError:
    print('file error')

# 上面那种情况如果出现了异常将导致读取流没有关闭
# 也就是close()没有运行
# 改进如下

try:
    out1 = open('man_data.txt', 'w')
    out2 = open('other_data.txt', 'w')
    print(man, file=out1)
    print(other, file=out2)
except IOError:
    print('file error')
finally:
    out1.close()
    out2.close()


'''这里书上说了一个‘字符串是不可变的’
    例如你使用了转换成大写，解释器会得到该字符串的一个副本，然后将其转换并将得到的结果返回给你
    不可变--你不知道还有那些变量指向摸个特定的字符串
    '''

# 还有一点，如果你要读一个文件，而这个文件不存在，那么对应的数据对象就不会被创建

try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError:
    print('file error')
finally:
    data.close()

# 上面会出异常,调用close时由于data未创建，下边是改进版

try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError:
    print('file error')
# locals()返回当前作用域中定义的所有名的一个集合
finally:
    if 'data' in locals():
        data.close()


# 但是到了这一步你依然不知道到底发生了什么

try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as err:
    print('file error' + str(err))
# locals()返回当前作用域中定义的所有名的一个集合
finally:
    if 'data' in locals():
        data.close()


try:
    with open('its.txt', "w") as data:
        print("It's ...", file=data)
except IOError as err:
    print('File error: ' + str(err))
