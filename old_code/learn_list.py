# 对list的渐进使用
"""据说这样
可以使用多行注释
"""
movies = ["the holy gails", 1975, "terry jones", ["gtaham", ["eric idle"]]]

# count = 0
# while count < len(movies):
#     print(movies[count])
#     count = count + 1
# movies.append("a")
# print(movies)

# 第三种
def deal_with_list (the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            deal_with_list(each_item)
        else:
            print(each_item)


# 改进
# 缺省参数可以使用户用不同方式都能调用这个函数，并且不会因为修改了参数的数目而导致此前版本的函数出现错误
# 如果参数里使用负数例如-1就会关闭缩进

def new_deal_with_list(the_list, level=0):
    """
        这个函数有一个位置参数，名为"the_list",
        这可以是任何Python列表（包含或不包含嵌套的列表）
        所提供列表中的各个数据项会（递归的）打印到屏幕上，而且各占一行
    :param the_list: 可以是任何Python列表（包含或不包含嵌套的列表）
    :param level: 用于产生一个递归的缩进，缺省值为0，使用负数可以关闭缩进
    :return: 无返回值
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            new_deal_with_list(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)


# 第三次改进，增加一个可选的参数indent来判断是否需要缩进
def last_deal_with_list(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            last_deal_with_list(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)


last_deal_with_list(movies)
last_deal_with_list(movies, True)
