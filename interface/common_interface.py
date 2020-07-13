#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: common_interface.py
@date: 2020/6/30
"""
import os

from conf import settings
from db import models


def get_all_schools_interface():
    school_dir = os.path.join(settings.DB_PATH, 'School')

    if not os.path.exists(school_dir):
        return False, '没有学校，请先联系管理员'

    school_list = os.listdir(school_dir)
    return True, school_list


# 公共登录接口
def login_interface(username, password, user_type):
    # obj = None
    if user_type == 'admin':
        obj = models.Admin.select(username)
    elif user_type == 'student':
        obj = models.Student.select(username)
    elif user_type == 'teacher':
        obj = models.Teacher.select(username)
    else:
        return False, '角色不正确'

    if obj:
        if password == obj.pwd:

            return True, '登录成功'
        else:
            return False, '密码错误'
    else:
        return False, f'{username}不存在'


def get_all_courses_school(school_name):
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, '没有课程'
    return True, course_list