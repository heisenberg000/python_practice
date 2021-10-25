# -*- encoding: utf-8 -*-
'''
@File    :   tb_discount.py
@Time    :   2021/10/25 11:22:23
@Author  :   James 
@Desc    :   淘宝折扣计算
@Version :   1.0
'''

def mutildiscount(unit,quantity):
    # 多件折扣 3件7折 2件8折
    if unit >= 3:
        price = unit*quantity*0.7
    elif unit >= 2:
        price = unit * quantity * 0.8
    else:
        price = unit * quantity
    return price

def coudan2000():
    pass

def jordan_discount(unit,quantity,isMutildiscount,isCoupon):
    # jordan店铺折扣
    coupon = {
        '2000': {
            'name':'满2000减400',
            'price': 2000,
            'discount': 400
        },
        '1400': {
            'name':'满1400减200',
            'price': 1400,
            'discount': 200
        },
        '1100': {
            'name':'满1200减120',
            'price': 1100,
            'discount': 120
        },
        '800': {
            'name':'满800减70',
            'price': 800,
            'discount': 70
        },
        '500': {
            'name':'满500减40',
            'price': 500,
            'discount': 40
        }
    }
    price = unit * quantity
    if isMutildiscount:
        price = mutildiscount(unit,quantity)
    if isCoupon:
        


if __name__ == '__main__':
  pass
