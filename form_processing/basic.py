# -*- encoding: utf-8 -*-
'''
@File    :   basic.py
@Time    :   2021/10/25 15:46:43
@Author  :   James 
@Desc    :   基础
@Version :   1.0
'''

def discount(price): #定义装饰器函数
    if price() >= 500.0:        
        return lambda: price() * 0.9
    else:
        return lambda: price()

@discount
def Entirely(): #购物金额
    return 555.0

def outerNums(func):
    def inner(x, y):
        x, y = eval(input('Two numbers:'))
        return func(x, y)
    return inner

@outerNums
def plusNumbers(x, y):
    return x**2 + y**2


if __name__ == '__main__':
    a, b = 0, 0
    print('平方和:', plusNumbers(a, b))
