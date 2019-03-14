# @Time    : 2019/3/14 22:06
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
username = "Bob"
password = "123"
times = 0
flag = False


def outer(f):
    def inner():
        if global flag:
            f()
        else:
            if times >= 3:
                print("your count is lock")
            else:
                name = input("please input your username :")
                word = input("please input your password :")
                if name == username and word == password:
                    print(" Welcom to shopping")
                    global flag = True
                else:
                    print("username or password is wrong")
                    global times = global times + 1







