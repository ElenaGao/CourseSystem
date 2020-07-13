#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: src.py
@date: 2020/6/29
"""

from core import admin
from core import student
from core import teacher

func_dict = {
    '0': None,
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


def run():
    while True:
        print("""
        ========welcome to course system=========
            0. 退出
            1. 管理员功能
            2. 学生功能
            3. 老师功能       
        
        =============END=========================
        """)

        choice = input('请输入功能编号：').strip()

        if not isinstance(int(choice), int):
            print('请输入数字编号')
            continue

        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        if choice == '0':
            print('退出选课系统')
            break

        func_dict.get(choice)()
