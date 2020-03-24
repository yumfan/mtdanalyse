# -*- coding:utf-8 -*-
# Python实现正态分布
# 绘制正态分布概率密度函数
import numpy as np
import matplotlib.pyplot as plt
import math

u = 0  # 均值μ
u01 = -2
#sig = math.sqrt(0.2)  # 标准差δ
sig=1

#samples=[154,156,149,148,150,151]
#samples = np.random.normal(100, 200, size=100)
#plt.hist(samples, bins=100, normed=True, histtype='stepfilled', label='bins=100')


x_1=np.linspace(32441,33095,50)
x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
print(x)
print("=" * 20)
print(y_sig)
plt.plot(x_1, y_sig, "r-", linewidth=2)
plt.grid(True)
plt.show()