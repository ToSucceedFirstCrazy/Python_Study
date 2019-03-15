# @Time    : 2019/3/13 22:57
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
# ________________初版________________________________
# import time
#
#
# def foo():
#     start_time = time.time()
#     print("foo")
#     time.sleep(2)
#     end_time = time.time()
#     print("spend %s" % (end_time-start_time))
#
#
# def too():
#     start_time = time.time()
#     print("too")
#     time.sleep(3)
#     end_time = time.time()
#     print("spend %s" % (end_time-start_time))
#
#
# foo()
# too()
# ___________________升级版_____________________
# import time
#
#
# def foo():
#     print("foo")
#     time.sleep(2)
#
#
# def too():
#     print("too")
#     time.sleep(3)
#
#
# def spend_time(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print("spend %s" % (end_time - start_time))
#
#
# spend_time(too)
# spend_time(foo)
# ________________________高级版________________________________
# import time
#
#
# def foo():
#     print("foo")
#     time.sleep(2)
#
#
# def too():
#     print("too")
#     time.sleep(3)
#
#
# def spend_time(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print("spend %s" % (end_time - start_time))
#     return inner
#
#
# foo = spend_time(foo)
# foo()


# _______________________特级版_________________________
# import time
#
#
# def spend_time(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print("spend %s" % (end_time - start_time))
#     return inner
#
#
# @spend_time     # foo = spend_time(foo)
# def foo():
#     print("foo")
#     time.sleep(2)
#
#
# @spend_time
# def too():
#     print("too")
#     time.sleep(3)
#
#
# foo()
# too()


# __________________终极版________________________


def logger(flag):

    def outer(f):
        def inner(*x, **y):
            f(*x, **y)
            print("装饰器")
            if flag:
                print("添加日志")
            else:
                print("不添加日志")
        return inner
    return outer


@logger(True)
def adder(*a, **b):
    sums = 0
    for i in a:
        sums += i
    print(sums)


@logger(False)
def counts(*a, **b):
    x = 1
    for i in a:
        x = x * i
    print(x)


adder(1, 5, 4, 5, 6)
counts(1, 2, 3, 4, 5)
