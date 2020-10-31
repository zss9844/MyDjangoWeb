# -*- coding: utf-8 -*-
#   @Time    : 2020/2/11 21:03
#   @Author  : 南国旧梦i
#   @FileName: test1.py
#   @Software: PyCharm
import requests

from cx_homework2 import func, mobile_func
from cx_homework2.func import get_course_list

conv = requests.session()

conv_login = func.login(conv=conv)  # 登录

course_list = mobile_func.get_course(conv_login)

print(mobile_func.get_work(conv_login,course_list))

print("登录成功")

course_list = get_course_list(conv_login)  # 获取课程对应url
# 返回一个含有所有课程名称和url的列表

print(course_list)
#
#
# print(course_work_list = get_course_work(conv_login, course_list))
# 返回一个含有所有课程名称和作业url的列表
#
# all_work_info_tag_list = get_work_info(conv_login,course_work_list)
# 返回一个含有所有待做作业tag的列表
#
# all_work_info_dict_list = parse_work(all_work_info_tag_list)
# 返回一个含有所有待做作业信息的列表

#print(all_work_info_dict_list)


#work_info_list = get_work_info(conv_login, course_list)




# course_info_dict = backclazzdata(conv_login) # 抓取课程列表

# gettask(course_info_dict,conv_login)
