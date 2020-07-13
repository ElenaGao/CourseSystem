#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: admin.py
@date: 2020/6/29
"""
from interface import admin_interface
from lib import common
from interface import common_interface

admin_info = {
    'user': None,
}


def register():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        if password == re_password:
            flag, msg = admin_interface.admin_register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新输入')


def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(username, password, user_type='admin')
        if flag:
            admin_info['user'] = username  # 记录当前用户登录状态
            print(msg)
            break
        else:
            print(msg)


@common.auth('admin')
def create_school():
    school_name = input('请输入学校名称：').strip()
    school_addr = input('请输入学校地址：').strip()

    flag, msg = admin_interface.admin_create_school_interface(school_name, school_addr, admin_info['user'])
    if flag:
        print(msg)

    else:
        print(msg)


@common.auth('admin')
def create_course():
    while True:
        # 1. 管理员先选择学校，调用接口，获取所有学校的名称并打印
        flag, school_list = common_interface.get_all_schools_interface()
        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'编号:{index}    学校名：{school_name}')

        choice = input('请输入学校编号：').strip()

        if not choice.isdigit():
            print('请输入数字')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('请输入正确编号！')
            continue

        # 2. 选择学校后，再输入课程名称
        school_name = school_list[choice]
        course_name = input('请输入需要创建的课程名称：').strip()

        # 3. 调用创建课程接口，管理员对象去创建课程
        flag, msg = admin_interface.admin_create_course_interface(school_name, course_name, admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师的名字：').strip()
        flag, msg = admin_interface.create_teacher_interface(teacher_name, admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dict = {
    '0': None,
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print("""
        管理员操作：
            0. 退出
            1. 注册
            2. 登录
            3.创建学校
            4.创建课程
            5.创建讲师
        """)

        choice = input('请输入功能编号：').strip()

        if not isinstance(int(choice), int):
            print('请输入数字编号')
            continue

        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        if choice == '0':
            print('退出管理员页面')
            break

        func_dict.get(choice)()
