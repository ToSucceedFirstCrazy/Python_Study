# @Time    : 2019/3/14 22:06
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
user = "Bob"
passwd = "123"
times = 0
login_status = False
status = True


def login(f):
    def inner():
        global times
        global login_status
        if not login_status:
            if times < 3:
                username = input("please input username:")
                password = input("please input password:")
                if user == username and passwd == password:
                    print("welcome......")
                    f()
                    login_status = True
                else:
                    print("username or password is wrong!!!")
                    times += 1
            else:
                print("your count is locked")

        else:
            f()
    return inner


@login
def book():
    print("book")


@login
def shoes():
    print("shoes")


@login
def food():
    print("food")


while status:
    choice = int(input("________________________\n"
          "________1.book__________\n"
          "________2.shoes_________\n"
          "________3.food__________\n"
          "________4.exit__________\n"
          "________________________\n"
          "please choice your list:\n"))
    if choice == 1:
        book()
    elif choice == 2:
        shoes()
    elif choice == 3:
        food()
    elif choice == 4:
        status = False
        print("bay~~~")
    else:
        print("your choice is wrong!!!")






