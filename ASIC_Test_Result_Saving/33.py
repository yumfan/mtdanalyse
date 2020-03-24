import matplotlib.pyplot as plt
from pylab import *  # 支持中文

mpl.rcParams['font.sans-serif'] = ['SimHei']

"""条形图bar"""
x = ['10/Q1', '10/Q3', '11/Q1', '11/Q3', '12/Q1', '12/Q3', '13/Q1', '13/Q3', '14/Q1', '14/Q3', '15/Q1', '15/Q3',
     '16/Q1', '16/Q3', '17/Q1', '17/Q3']
y = [20, 35, 39, 62, 87, 114, 140, 169, 187, 211, 225, 239, 241, 247, 251, 258]

# plt.bar([1,3,5,7,9],[5,2,7,8,2],label='Example One',color='b')#plt.bar创建条形图
# plt.bar([2,4,6,8,10],[8,6,2,5,6],label='Example Two',color='g')

plt.bar(range(16), y, color='lightsteelblue')
plt.plot(range(16), y, marker='o', color='coral')  # coral
plt.xticks(range(16), x)
plt.xlabel('年份/季度')
plt.ylabel("月活跃用户数(单位：百万)")
plt.legend()
plt.show()
