> 链接：https://www.nowcoder.com/questionTerminal/5d2405da8d364eafbaca1de9bc2a0d4e
> 
> 来源：牛客网
> 
> 近期某商场由于周年庆，开启了“0元购”活动。活动中，消费者可以通过组合手中的代金券，实现0元购买指定商品。聪明的小团想要用算法来帮助他快速计算：对于指定价格的商品，使用代金券凑出其价格即可，但所使用的代金券总面额不可超过商品价格。由于代金券数量有限，使用较少的代金券张数则可以实现价值最大化，即最佳优惠。假设现有100元的商品，而代金券有50元、30元、20元、5元四种，则最佳优惠是两张50元面额的代金券；而如果现有65元的商品，则最佳优惠是两张30元代金券以及一张5元代金券。请你帮助小团使用一段代码来实现代金券计算。
> 
> 
> 输入描述:
> 
> 多组输入输出，读到s=0时结束
> 输入可以有多个测试样例，每个测试由两行组成。
> 其中第一行包含一个整数P，表示商品的价格，1≤P≤10000；输入P为0时表示结束。
> 第二行包含若干整数，使用空格分割。其中第一个整数N（1≤N≤20）表示有多少种代金券，其后跟随M个整数，表示手中持有的代金券面额（1≤N≤1000），每种代金券数量不限。
> 
> 输出描述:
> 
> 找到最少张数的代金券，使其面额恰好等于商品价格。输出所使用的代金券数量；
> 如果有多个最优解，只输出其中一种即可；
> 如果无解，则需输出“Impossible”。

分析：

这是个**完全背包**问题。

先穷举一把，以65元为例。

* 情况1：先拿最大的50元。然后5+5+5。4张
* 情况2：先拿30元。30+30+5，3张。
* 情况3：先拿20元，20+20+20+5，4张；
* 情况4：只拿5元，13张。

这四种情况下，每次拿一张之后，都去找剩下的钱可以拿到最大的是哪个。那么，65元可以拆解如下：
* 65 = 50 + 15
* 65 = 30 + 35
* 65 = 20 + 45
* 65 = 5 + 60

然后比哪个是最小值。写Python代码如下：

代码有误，需要修改

```Python
from sys import maxsize as MAX

def solution(n, amount, vouchers):
    # n为价钱数
    # vouchers即为代金券面值
    # amount为种类数

    # 判空是好习惯。如果是空数组，那么直接返回-1不好么
    if not vouchers:
        return -1
    
    # 对原数组进行排序
    vouchers = sorted(vouchers)

    # 边界条件1：如果商品价格比最小面值优惠券还要小的话，那就直接等于1张
    if n <= vouchers[0]:
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
        if n >= voucher:
            tmp = 1 + solution(n - voucher, amount vouchers)
            if tmp < res:
                res = tmp
    
    return res
```

但是递归会导致大量重复计算，数据量一上来只有等着爆栈的份儿。所以，如果能用额外空间存起来已经计算的结果呢？

于是，动态规划第一步：**以空间换时间**，在《算法导论》中叫做**time-memory trade-off**。实际操作中，既要时间度低又要空间复杂度低的情况几乎不存在，要么时转空要么空转时。

动态第一式：

```Python
from sys import maxsize as MAX

def solution(n, amount, vouchers):
    # n为价钱数
    # vouchers即为代金券面值
    # amount为种类数

    # 判空是好习惯。如果是空数组，那么直接返回-1
    if not vouchers:
        return -1
    
    # 对原数组进行排序，让最小的排前面
    vouchers = sorted(vouchers)

    # 申请额外空间，用于存放重复的计算结果
    dp = [MAX for i in range(n + 1)]
    dp[0] = -1
    for i in range(1, n + 1):
        if (i < vouchers[0]) or (i in vouchers):
            # 如果商品价值比最小面值的优惠券都小
            # 或者刚好等于一个面值
            # 那么一张即可
            dp[i] = 1
        else:
            for voucher in vouchers:
                if (i - voucher) > 0:
                    tmp = 1 + dp[i - voucher]
                    if tmp < dp[i]:
                        dp[i] = tmp
    
    return dp[n]
```

最终题解：

因为牛客网要自己写输入输出，且不能小于5的抵5，所以最终提交版本如下(于2021.8.7优化代码)：

```Python
#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from sys import stdin, stdout
from sys import maxsize as MAX

def solution(price, vouchers):
    # 根据题意，无需判空。故没有判空
    vouchers = sorted(vouchers)
    
    # 动态规划数组
    dp = [MAX for i in range(price + 1)]
    for voucher in vouchers:
        if voucher <= price:
            dp[voucher] = 1
    
    for i in range(price + 1):
        for voucher in vouchers:
            if (i - voucher) > 0:
                dp[i] = min(dp[i], 1 + dp[i - voucher])
    
    return dp[price]

if __name__ == '__main__':
    while price := int(stdin.readline().strip()): # 本行在Python 3.8以后可用。:=（冒等运算符）
        if not price: # 输0就跳出
            break
        vouchers = list(map(int, stdin.readline().strip().split()))
        
        res = solution(price, vouchers[1::])
        
        if res == MAX:
            stdout.write('Impossible\n')
        else:
            stdout.write('%d\n'%res)
```