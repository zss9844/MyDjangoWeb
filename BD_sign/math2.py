# -*- coding: utf-8 -*-
#   @Time    : 2020/6/7 19:47
#   @Author  : 南国旧梦i
#   @FileName: math2.py
#   @Software: PyCharm
from sympy import *
import numpy as np
# 假设多元函数是二维形式
# x_init为二维向量(x1, x2)
def newton_dou(step, x_init, obj):
    i = 1 # 记录迭代次数的变量
    while i <= step:
        if i == 1:
            grandient_obj = np.array([diff(obj, x1).subs(x1, x_init[0]).subs(x2, x_init[1]), diff(obj, x2).subs(x1, x_init[0]).subs(x2, x_init[1])], dtype=float) # 初始点的梯度值
            hessian_obj = np.array([[diff(obj, x1, 2), diff(diff(obj, x1), x2)], [diff(diff(obj, x2), x1), diff(obj, x2, 2)]], dtype=float) # 初始点的hessian矩阵
            print(hessian_obj)
            inverse = np.linalg.inv(hessian_obj) # hessian矩阵求逆
            print(inverse)
            x_new = x_init - np.matmul(inverse, grandient_obj) # 第一次迭代公式
            print(x_new)
            # print('迭代第%d次：%.5f' %(i, x_new))
            i = i + 1
        else:
            grandient_obj = np.array([diff(obj, x1).subs(x1, x_new[0]).subs(x2, x_new[1]), diff(obj, x2).subs(x1, x_new[0]).subs(x2, x_new[1])], dtype=float) # 当前点的梯度值
            hessian_obj = np.array([[diff(obj, x1, 2), diff(diff(obj, x1), x2)], [diff(diff(obj, x2), x1), diff(obj, x2, 2)]], dtype=float) # 当前点的hessian矩阵
            inverse = np.linalg.inv(hessian_obj) # hessian矩阵求逆
            x_new = x_new - np.matmul(inverse, grandient_obj) # 迭代公式
            print(x_new)
            # print('迭代第%d次：%.5f' % (i, x_new))
            i = i + 1
    return x_new

x0 = np.array([0, 0], dtype=float)
x1 = symbols("x1")
x2 = symbols("x2")
newton_dou(5, x0, x1**2+2*x2**2-2*x1*x2-2*x2)