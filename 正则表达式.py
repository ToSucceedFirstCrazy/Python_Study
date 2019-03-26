# @Time    : 2019/3/26 21:43
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
# 正则表达式是用来干嘛的：
#         匹配 字符串
# string 提供的是完全匹配
# 引入正则： 模糊匹配

# 正则表达式的方法：
 所有结果都返回一个列表里面
 返回一个对（象，


# s = "hello world"
# print(s.find("w"))
# ret = s.replace("ll", "xx")
# print(ret)
# print(s.split("l"))
# print(help(re))

import re

ret = re.findall("w..l", "hello world")
print(ret)

