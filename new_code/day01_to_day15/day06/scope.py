# def foo():
#     b = 'hello'

#     def bar():  # Python中可以在函数内部再定义函数
#         c = True
#         print(a)
#         print(b)
#         print(c)

#     bar()
#     # print(c)  # NameError: name 'c' is not defined


# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

"""
a-----全局变量-----全局作用域
b-----局部变量-----局部作用域-----
        在foo函数中的bar函数使用到变量b时按照
        局部作用域->全局作用域->内置作用域 的顺序查找
        “内置作用域”就是Python内置的那些隐含标识符min、len等都属于内置作用域
        因此在bar函数里找不到后向外层查找
c-----局部变量-----局部作用域
"""

"""
希望通过函数调用修改全局变量a的值，但实际上下面的代码是做不到的
"""

# def foo():
#     a = 200
#     print(a)  # 200


# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100

"""
原因
    在函数foo中定义了一个变量a，这个变量a与全局作用域中的a不是同一个变量
    以foo.a的方式来理解吧，就是实际上它的名字是“函数foo里的变量a”
如果我们希望在foo函数中修改全局作用域中的a，代码如下所示
"""

# def foo():
#     #用global关键字指代该变量来自全局作用域
#     global a
#     #如果全局作用域中没有a则初始化
#     a = 200
#     print(a)  # 200

# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200

#使用nonlocal关键字修改嵌套作用域的变量 

# def make_counter(): 
#     count = 0 
#     def counter(): 
#         nonlocal count 
#         count += 1 
#         return count 
#     return counter 
# #突然做出了闭包的效果
# if __name__ == "__main__":
#     mc = make_counter() 
#     print(mc())
#     print(mc())
#     print(mc())

def scope_test():
    def do_local():
        spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
    def do_nonlocal():
        nonlocal  spam        #使用外层的spam变量
        spam = "nonlocal spam"
    def do_global():
        #global只修改全局作用域中的变量，因此它跳出这个函数(scope_test)去到外面找到了spam，
        # 或者说它发现没有spam于是相当于声明了这一变量
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()   
    print("After global assignment:",spam)

spam = 'really' #这一行去掉也可以,因为在函数中使用global关键字会在全局不存在变量时自动声明该变量
scope_test()
print("In global scope:",spam)
