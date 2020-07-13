#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: common.py
@date: 2020/6/29
"""
from functools import wraps


# 多用户登录认证装饰器

def auth(role):
    """

    :param role: 角色，管理员，学生，老师
    :return:
    """
    from core import admin, student, teacher

    def login_auth(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()

            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()

            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()

            else:
                print('当前视图没有权限')

        return wrapper

    return login_auth



