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

print(man)
print(other)

# 与JAVA一样，如果你不存在这个文件来写入，它会自动创建这一文件来写入
# 但是如果这个文件已经存在了呢？它会清空它现有的内容
# 要追加到一个文件，需要使用访问模式a
# 想要打开一个文件来完成写和读，需要使用w+模式
# 还有一点，如果你要读一个文件，而这个文件不存在，那么对应的数据对象就不会被创建
out = open("data.out", "w")

print("Norwegian Blues stun easily.", file=out)

out.close()