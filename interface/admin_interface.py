#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: admin_interface.py
@date: 2020/6/30
"""
from db import models


def admin_register_interface(username, password):
    # 判断用户是否存在
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, f'用户{username}已存在'

    admin_obj = models.Admin(username, password)
    admin_obj.save()
    return True, f'用户{username}注册成功'


def admin_create_school_interface(school_name, school_addr, admin_name):
    # 查看学校是否已存在
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, f'{school_name}已存在'

    # 若不存在，则创建学校（ps: 由管理员对象来创建）
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_addr)
    return True, f'{school_name}学校创建成功'


def admin_create_course_interface(school_name, course_name, admin_name):
    # 先获取学校对象中的课程列表，判断当前课程是否存在课程列表中
    school_obj = models.School.select(school_name)
    if course_name in school_obj.course_list:
        return False, '当前课程已存在!'

    # 若课程不存在，则创建课程，由管理员来创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj, course_name)
    return True, f'{course_name}课程创建成功'


def create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False, f'{teacher_name}老师已存在'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)

    return True, f'{teacher_name}老师创建成功'
