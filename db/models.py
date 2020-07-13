#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: models.py
@date: 2020/6/29
"""
from db import db_handler

"""
用于存放类
"""


class Base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select(cls, username)
        return obj

    def save(self):
        db_handler.save(self)


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        # 调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()
        # 获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        # 更新学校数据
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr
        self.course_list = []


class Student(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.course_list = []  # {"course_name":0}
        self.score = {}
        self.school = None

    def add_school(self, school_name):
        self.school = school_name
        self.save()

    def choice_course(self, course_name):
        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save()
        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list = []

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def show_course(self):
        return self.course_list

    def get_student(self, course_name):
        course_obj = Course.select(course_name)
        if course_obj:
            return course_obj.student_list

    def change_score(self, student_name, course_name, score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()
