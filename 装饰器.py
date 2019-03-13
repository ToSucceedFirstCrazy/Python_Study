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
import time


def foo():
    print("foo")
    time.sleep(2)


def too():
    print("too")
    time.sleep(3)


def spend_time(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print("spend %s" % (end_time - start_time))
    return inner


foo = spend_time(foo)
foo()


