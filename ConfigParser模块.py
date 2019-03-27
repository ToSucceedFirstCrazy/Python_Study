# @Time    : 2019/3/26 20:31
# @Author  : ToSucceedFirstCrazy 
# @Email   : 179942072@qq.com
# @Wish    : Good Good Study Day Day Up
# @Blog    : https://github.com/ToSucceedFirstCrazy/Python_Study
# import configparser     # 配置文件模块
#
# config = configparser.ConfigParser()
#
#
# config["DEFAULT"] = {"ServerAliveInterval": "45",
#                      "Compression": "yes",
#                      "CompressionLevel": "9",
#                      "Forwardx11": "yes"}
# config["bitbucket.org"] = {"User": "hg"}
# config["topsecret.server.com"] = {"Host Port": "5002"}
#
# with open("example.ini", "w") as configfile:
#     config.write(configfile)

import configparser

config = configparser.ConfigParser()
config.read("example.ini")
# print(config.sections())
# print(config.defaults())
# print(config["DEFAULT"]["CompressionLevel"])
# for key in config["bitbucket.org"]:
#     print(key)
# print("_____________")
# for key in config:
#     print(key)







