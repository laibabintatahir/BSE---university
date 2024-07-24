# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:39:15 2024

@author: Laiba Binta Tahir
"""

#Diamond Problem
class Class1:
    def m(self):
        print("Class1 method m")

class Class2(Class1):
    def m(self):
        print("Class2 method m")

class Class3(Class1):
    def m(self):
        print("Class3 method m")

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()


#Multiple inheritence

class Parent1:
    def feature1(self):
        print("Feature 1 from Parent1")

class Parent2:
    def feature2(self):
        print("Feature 2 from Parent2")

class Child(Parent1, Parent2):
    def feature3(self):
        print("Feature 3 from Child")

# Creating an instance of Child
child_instance = Child()

# Accessing features from both Parent1 and Parent2
child_instance.feature1()  # Output: Feature 1 from Parent1
child_instance.feature2()  # Output: Feature 2 from Parent2
child_instance.feature3()  # Output: Feature 3 from Child
