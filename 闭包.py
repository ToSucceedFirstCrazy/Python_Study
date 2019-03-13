# @Time    : 2019/3/13 23:35
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
# 作用域：L - E - G - B
# a = 10
#
#
# def out():
#     b = 20
#
#     def inner():
#          c = 30
#          print(a)
#          print(b)
#          print(c)
#          return 1
#     inner()
#
#
# out()
# ___________________高阶函数____________________
# 高阶函数：
#         1.函数名可以做为参数输入
#         2.函数名可以作为返回值

# ___________________闭包__________________________
# 闭包：
#         如果在一个内部函数里，对外部作用域（但不是在全局作用域）
#         的变量进行引用，那么内部函数就被认为是闭包


def outer():
    x = 10

    def inner():
        print(x)

    return inner


x = outer()
x()
