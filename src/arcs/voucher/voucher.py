#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from sys import maxsize as MAX

def solution(n, l, vouchers):
    # n为价钱数
    # vouchers即为代金券面值
    # l为种类数

    # 判空是好习惯。如果是空数组，那么直接返回-1不好么
    if not vouchers:
        return -1
    
    # 对原数组进行排序，让最大的排前面
    vouchers = sorted(vouchers, reverse = True)

    # 边界条件1：如果商品价格比最小面值优惠券还要小的话，那就直接等于1张
    if n <= vouchers[-1]:
        return 1
    
    # 边界条件2：如果商品价格和面值刚好相等，那么直接一张
    for voucher in vouchers:
        if n == voucher:
            return 1
    
    # 递推公式
    '''
    65的解决方式是这样的：
    * 50 + 15
    * 30 + 35
    * 20 + 45
    * 5 + 60

    四个当中找最小
    '''
    res = MAX # 要足够大
    for voucher in vouchers:
        # 递归
        tmp = 1 + solution(n - voucher, l, vouchers)
        if tmp < res:
            res = tmp
    
    return res

if __name__ == '__main__':
    vouchers = [50, 30, 20, 5]
    print(solution(65, 4, vouchers))