#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: student.py
@date: 2020/6/29
"""

from lib import common
from interface import student_interface
from interface import common_interface

student_info = {
    'user': None,
}


def register():
    while True:
        username = input('请输入注册的学生性名：').strip()
        password = input('请输入注册的密码：').strip()
        re_password = input('请确认密码：').strip()

        if password == re_password:
            flag, msg = student_interface.register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('2次输入密码不正确，请重新输入')


def login():
    while True:
        username = input('请输入登录学生姓名：').strip()
        password = input('请输入登录密码：').strip()

        flag, msg = common_interface.login_interface(username, password, user_type='student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)


@common.auth('student')
def select_school():
    while True:
        flag, school_list = common_interface.get_all_schools_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f'编号：{index}   学校名：{school_name}')

        choice = input('请输入学校编号').strip()
        if not choice.isdigit():
            print('请输入数字编号')
            continue

        choice = int(choice)
        if choice not in range(len(school_list)):
            print('请输入正确编号')
            continue

        school_name = school_list[choice]
        flag, msg = student_interface.add_school_interface(school_name, student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('student')
def select_course():
    # 先获取当前学生所在学校的课程列表，再选择对应的课程
    while True:
        flag, course_list = student_interface.get_course_interface(student_info['user'])
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'课程编号:{index}   课程名称：{course_name}')

        choice = input('请输入课程编号').strip()
        if not choice.isdigit():
            print('请输入数字编号')
            continue

        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确编号')
            continue

        course_name = course_list[choice]
        flag, msg = student_interface.choice_course_interface(course_name, student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('student')
def check_score():
    score = student_interface.check_score_interface(student_info['user'])
    if not score:
        print('没有选择课程')
    print(score)


func_dict = {
    '0': None,
    '1': register,
    '2': login,
    '3': select_school,
    '4': select_course,
    '5': check_score,
}


def student_view():
    while True:
        print("""
        学生操作：
         0. 退出
         1.注册
         2.登录
         3.选择校区
         4.选择课程（先选择校区，再选择校区中的某一门课程）
         5.查看分数
        """)

        choice = input('请输入功能编号：').strip()

        if not isinstance(int(choice), int):
            print('请输入数字编号')
            continue

        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        if choice == '0':
            print('退出学生页面')
            break

        func_dict.get(choice)()
