# @Time    : 2019/3/25 20:55
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
# import random
#
#
# def v_code():
#     code = ""
#     for i in range(5):
#         add_num = random.randrange(10)
#         code += str(add_num)
#     print(code)
#
# v_code()

import random


# def v_code():
#     code = ""
#     x = random.randint(1, 5)
#     y = 5 - x
#     for i in range(x):
#         code += chr(random.randrange(97, 122))
#     for j in range(y):
#         code += str(random.randrange(10))
#     print(code)
#
#
# v_code()


import random


def v_code():
    code = ""
    for i in range(5):
        add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(add)
    print(code)


v_code()

