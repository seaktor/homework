# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def program(number):
    total=0
    a=1
    while a<=number:
        total=total+1/a
        a=a+1
    return total

result=program(1000)

print(result)


def program(number):
    total=0
    a=1
    while a<=number:
        total=total+1/a
        a=a+1
    print(total)

program(1000)


def math(number):
    total=0
    a=1
    while a<=number:
        total=total+a
        a=a+1
    return total

def eng(number):
    total=0
    a=1
    q=1
    w=1
    while a<=number:
        total=q/w
        a=a+1
        w=a+w
        q=a*q
    return total

print(math(1000)+eng(10))



        
