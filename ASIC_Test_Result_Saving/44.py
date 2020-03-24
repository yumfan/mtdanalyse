import matplotlib
import pandas as pd # 导入另一个包“pandas” 命名为 pd，理解成pandas是在 numpy 基础上的升级包
import numpy as np    #导入一个数据分析用的包“numpy” 命名为 np
import matplotlib.pyplot as plt   # 导入 matplotlib 命名为 plt，类似 matlab，集成了许多可视化命令

#jupyter 的魔术关键字（magic keywords）
#在文档中显示 matplotlib 包生成的图形
# 设置图形的风格
#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'

#data = pd.read_csv('stakes.csv') #载入数据文件
#data.head(5) #查看前5个头部数据
from pandas import DataFrame

data=[108.51,146.65,148.52,150.70,190.42]
#len(data) #查看数据长度
#time = [142,144,146,148,152,154,156,158,160,162]#把数据集中的 time 定义为 time
time =DataFrame(data)
#mean均值，是正态分布的中心，把 数据集中的均值 定义为 mean
mean = time.mean()
mean=mean[0]
#S.D.标准差，把数据集中的标准差 定义为 std
std = time.std()
std=std[0]

def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))            #y_sig = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    print(pdf)
    return pdf


# 设定 x 轴前两个数字是 X 轴的开始和结束，第三个数字表示步长，或者区间的间隔长度
x = np.arange(100,200,0.1)
mean=x.mean()
mean=149
std=x.std()
std=1
#设定 y 轴，载入刚才的正态分布函数
y = normfun(x, mean, std)
plt.plot(x,y)
#画出直方图，最后的“normed”参数，是赋范的意思，数学概念
plt2=plt.twinx()
plt2.hist(time, bins=10, rwidth=0.9, normed=True)
#plt2.plot(x,y)
plt.title('Time distribution')
plt.xlabel('Time')
plt.ylabel('Probability')
#输出
plt.show()