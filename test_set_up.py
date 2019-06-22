import learn_list

cast = ["palin", "chese", ["idle", "eric", ["fallin"]]]

learn_list.deal_with_list(cast)

# 在这里（第二天）我修改了learn_list 的代码，此时运行就不会再执行那些多余的代码了
# 但是要注意，那个打包的模块还是为更新的，如果要用模块的话，就得重新打包

"""可以看见
    在import一个模块的瞬间
    即使你什么也没做
    它也会自动执行该模块内部的
    可以被执行的语句
    在learn_list模块中
    我们定义了的循环就被调用了
    所以直接打了一堆没用的字出来
    """