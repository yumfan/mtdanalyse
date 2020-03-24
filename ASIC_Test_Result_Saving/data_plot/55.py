import matplotlib.pyplot as plt
import numpy as np

# 数据
mu = 100  # 均值
sigma = 20  # 方差
# 2000个数据
x = mu + sigma*np.random.randn(2000)



# 画图 bins:条形的个数， normed：是否标准化
plt.hist(x=x, bins=10)


# 展示
plt.show()