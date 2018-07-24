#! usr/lib/env
#! -*- coding: utf-8 -*-

# from collections import OrderedDict
# from random import randint
#
# my_sports = OrderedDict()
# my_sports['name'] = 'bob'
# my_sports['age'] = 23
# my_sports['sex'] = '男'
# my_sports['school'] = 'china'
#
# for key, value in my_sports.items():
#     print(key, value)
#
# # 骰子
# class Die():
#     def __init__(self, sides = 6):
#         self.sides = sides
#     def roll_die(self):
#         x = randint(1, self.sides)
#         print('The radomrange is ' + str(x))
# six_die = Die()
# six_die.roll_die()
# six_die.roll_die()
# six_die.roll_die()
# six_die.roll_die()
# six_die.roll_die()
# six_die.roll_die()
#
filename = 'text_file/pi_digits.txt'
# with open(filename) as file_object:
#     content = file_object.readlines()
#     # print(content[:53] + '...')
#     # print(content)
# string = ''
# for line in content:
#     string += line.strip()
# print(string[:32] + '...')
#
# # Python学习笔记
# learn_python = 'text_file/learning_python.txt'
# with open(learn_python) as python_file:
#     tmp_text = python_file.readlines()
#     # 直接读取
#     # print(python_file.read())
# # 遍历读取
# # for line in tmp_text:
# #     print(line.rstrip())
#
# # 存储在列表中
# list = []
# for line in tmp_text:
#     # line.replace('Python', 'C')
#     list.append(line.replace('Python', 'C'))
# print(list)


# 写入文件  write
# w+模式下, 写入的时候会清空之前文件里面的内容, 写入新的内容
# r+模式下, 写入的时候只会写入跟需要写入内容长度相同的内容, 之后的内容不会发生变化
# a模式下, 写入的时候在已有内容的后面写入
# with open(filename, 'a') as pi_file:
#     pi_file.write('I love programing')


# 访客, 写入用户输入的内容
guest_file = 'text_file/guest.txt'
active = True
with open(guest_file, 'a+') as guest_object:
    tmp_guest = guest_object.read()
    print(tmp_guest)
    while active:
        guest_object.seek(0)
        username = input('input your name: ')
        if username == 'q':
            break
        else:
                guest_object.write('\n' + username)
            # if tmp_guest:
            #     guest_object.write('\n' + username)
            # else:
            #     guest_object.write(username)
# while 1:
#     username = input('input your name: ')
#     if username == 'q':
#         break
#     else:
#         with open(guest_file, 'a+') as guest_object:
#             guest_object.seek(0)
#             tmp_guest = guest_object.read()
#
#             if tmp_guest:
#                 guest_object.write('\n' + username)
#             else:
#                 guest_object.write(username)

