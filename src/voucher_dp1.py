#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from sys import maxsize as MAX

def solution(n, amount, vouchers):
    # n为价钱数
    # vouchers即为代金券面值
    # amount为种类数

    # 判空是好习惯。如果是空数组，那么直接返回-1
    # 不过在原题没有太大必要判空
    # if not vouchers:
    #     return -1
    
    # 对原数组进行排序，让最小的排前面
    vouchers = sorted(vouchers)

    # 申请额外空间，用于存放重复的计算结果
    dp = [MAX for i in range(n + 1)]

    # 代码优化
    for voucher in vouchers:
        if voucher < len(vouchers):
            dp[voucher] = 1

    # for i in range(1, n + 1):
    for i in range(n + 1):
        # if (i < vouchers[0]) or (i in vouchers):
        #     # 如果商品价值比最小面值的优惠券都小
        #     # 或者刚好等于一个面值
        #     # 那么一张即可
        #     dp[i] = 1
        # else:
        for voucher in vouchers:
            if (i - voucher) > 0:
                dp[i] = min(dp[i], 1 + dp[i - voucher])
                    # 代码优化，底下的可以完全不要
                    # tmp = 1 + dp[i - voucher]
                    # if tmp < dp[i]:
                    #     dp[i] = tmp
    
    return dp[n]

if __name__ == '__main__':
    vouchers = [50, 30, 20, 5]
    print(solution(65, 4, vouchers))