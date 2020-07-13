#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: student_interface.py
@date: 2020/7/1
"""
from db import models


def register_interface(username, password):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, f'{username}学生已经存在'

    student_obj = models.Student(username, password)
    student_obj.save()
    return True, f'{username}学生注册成功'


def add_school_interface(school_name, student_name):
    # 判断当前学生是否存在学校
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, f'{student_name}已经选择过学校{school_name}'

    student_obj.add_school(school_name)
    return True, f'{student_name}选择学校{school_name}成功'


def get_course_interface(student_name):
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    if not school_name:
        return False, f'{student_name}学生没有学校，请先选择学校'

    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, f'{school_name}没有课程，请联系管理员'

    return True, course_list


def choice_course_interface(course_name, student_name):
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.course_list:
        return False, f'{course_name}课程已存在'
    student_obj.choice_course(course_name)
    return True, f'{course_name}课程添加成功'


def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.score:
        return student_obj.score
