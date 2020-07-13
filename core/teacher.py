#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: teacher.py
@date: 2020/6/29
"""
from interface import common_interface, teacher_interface
from lib import common

teacher_info = {
    'user': None,
}


def login():
    while True:
        username = input('请输入登录老师姓名：').strip()
        password = input('请输入登录密码：').strip()

        flag, msg = common_interface.login_interface(username, password, user_type='teacher')
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)


@common.auth('teacher')
def check_course():
    flag, course = teacher_interface.check_course_interface(teacher_info['user'])
    print(course)


@common.auth('teacher')
def choose_course():
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
        flag, course_list = common_interface.get_all_courses_school(school_name)
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'课程编号：{index}   课程名称：{course_name}')

        choice2 = input('请输入课程编号').strip()
        if not choice2.isdigit():
            print('请输入数字编号')
            continue

        choice2 = int(choice2)
        if choice2 not in range(len(course_list)):
            print('请输入正确编号')
            continue
        course_name = course_list[choice2]
        flag, msg = teacher_interface.add_course_interface(course_name, teacher_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('teacher')
def check_stu_from_course():
    while True:
        # 先列出老师的课程列表，查询对应的学生列表
        flag, course_list = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'课程编号：{index}  课程名称：{course_name}')

        choice = input('请输入课程编号：').strip()
        if not choice.isdigit():
            print('请输入数字编号')
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入编号有误')
            continue

        course_name = course_list[choice]

        flag, msg = teacher_interface.get_stu_interface(course_name, teacher_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth('teacher')
def change_score_from_student():
    while True:
        # 先列出老师的课程列表，查询对应的学生列表
        flag, course_list = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'课程编号：{index}  课程名称：{course_name}')

        choice = input('请输入课程编号：').strip()
        if not choice.isdigit():
            print('请输入数字编号')
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入编号有误')
            continue

        course_name = course_list[choice]

        flag, student_list = teacher_interface.get_stu_interface(course_name, teacher_info['user'])
        if not flag:
            print(student_list)
            break
        for index, student_name in enumerate(student_list):
            print(f'学生编号：{index}   学生姓名：{student_name}')

        student_name = input('请输入学生编号：').strip()
        if not student_name.isdigit():
            print('请输入数字编号')
            continue
        student_name = int(student_name)

        if student_name not in range(len(student_list)):
            print('输入编号有误')
            continue

        student_name = student_list[student_name]
        score = input('请输入修改的分数').strip()
        score = int(score)

        flag, msg = teacher_interface.change_score(student_name, course_name, score, teacher_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dict = {
    '0': None,
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student,
}


def teacher_view():
    while True:
        print("""
        老师操作：
             0. 退出
             1. 登录
             2. 查看教授课程
             3. 选择教授课程
             4. 查看课程下学生
             5. 修改学生分数
        """)

        choice = input('请输入功能编号：').strip()

        if not isinstance(int(choice), int):
            print('请输入数字编号')
            continue

        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        if choice == '0':
            print('退出老师页面')
            break

        func_dict.get(choice)()
