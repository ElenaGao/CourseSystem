#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: db_handler.py
@date: 2020/6/29
"""

import os
import pickle
from conf import settings


# 保存数据
def save(obj):
    """
    obj.__class__： 获取当前对象的类
    obj.__class__.__name__: 获取当前对象的类名
    :param obj:
    :return:
    """
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)

    # 以类名创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接当前用户的pickle文件路径，以用户名作为文件名
    user_path = os.path.join(user_dir_path, obj.user)

    # 打开文件，保存对象, pickle
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


# 查看数据
def select(cls, username):
    class_name = cls.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)
    user_path = os.path.join(user_dir_path, username)

    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj