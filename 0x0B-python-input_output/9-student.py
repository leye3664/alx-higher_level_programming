#!/usr/bin/python3
"""
File: 9-student.py
Desc: This module contains one class; Student
Author: Oluleye Olumide (leye)
Date Created: 02 Aug 2022
"""


class Student:
    """
    Reoresentation of the class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
