#!/usr/bin/python3

"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0
    num_H = 1
    num_Oper = 0
    copy_all = num_H

    while num_H < n:
        if n % num_H == 0:
            copy_all = num_H
            num_H += copy_all
            num_Oper += 2
        else:
            num_H += copy_all
            num_Oper += 1
    return num_Oper
