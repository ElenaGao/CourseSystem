#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: teacher_interface.py
@date: 2020/7/2
"""

from db import models


def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.show_course()

    if not course_list:
        return False, f'{teacher_name}没有选择课程'
    return True, course_list


def add_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if course_name in teacher_obj.course_list:
        return False, f'{course_name}已经存在'

    teacher_obj.add_course(course_name)
    return True, f'{course_name}添加成功'


def get_stu_interface(course_name, teacher_name):
    # 获取当前老师对象，调用获取课程下所有学生功能
    teacher_obj = models.Teacher.select(teacher_name)

    student_list = teacher_obj.get_student(course_name)
    if not student_list:
        return False, F'{course_name}没有学生'
    return True, student_list


def change_score(student_name, course_name, score, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    teacher_obj.change_score(student_name, course_name, score)
    return True, '修改成功'
