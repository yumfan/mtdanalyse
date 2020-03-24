import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# 正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
from pandas import DataFrame


def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf



mu = 0
#sigma = 0.1
s=np.random.normal(100, 40, size=100)
data=DataFrame(s)
mu=data.mean()[0]

sigma=data.std()[0]
#s=np.linspace(0,2,1)
# Python实现正态分布
# 绘制正态分布概率密度函数
#for i in range(len(s)):
    #sigma=s[i]
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)              #numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0),(在start和stop之间返回均匀间隔的数据)
y_sig = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
plt.plot(x, y_sig, "r-", linewidth=2,label="sigma=%s"%(sigma))
#x = np.arange(32400,33100,50)
#y_sig=normfun(x,mu,sigma)
#plt.bar(x,y_sig,fc='b',linewidth=0.1)
#plt.hist(y_sig, bins=10, rwidth=0.9, normed=True)
'''
plt.vlines(mu, 0, np.exp(-(mu - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma), colors="c",
           linestyles="dashed")
plt.vlines(mu + sigma, 0, np.exp(-(mu + sigma - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
           colors="k", linestyles="dotted")
plt.vlines(mu - sigma, 0, np.exp(-(mu - sigma - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
           colors="k", linestyles="dotted")
'''
#plt.xticks([mu - sigma, mu, mu + sigma], ['μ-σ', 'μ', 'μ+σ'])
plt.xlabel('Frequecy')
plt.ylabel('Latent Trait')
plt.title('Normal Distribution: $\mu = %.2f, $sigma=%.2f' % (mu, sigma))
plt.grid(True)
plt.legend()
plt.show()
