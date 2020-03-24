import matplotlib.pylab as plt # 导入绘图包
import matplotlib.pyplot as mp
from pylab import * #图像中的title,xlabel,ylabel均使用中文
import numpy as np

#使用自己下载的宋体库simsun.ttc，原始matplotlib不支持中文
#myfont = matplotlib.font_manager.FontProperties(fname="simsun.ttc")
mpl.rcParams['axes.unicode_minus'] = False

dates,y1 = np.loadtxt(r'C:\Users\fym12\PycharmProjects\ASIC_Test_Result_Saving\temp.csv', str,delimiter=',', usecols=(0,1), unpack=True,encoding='UTF-8')
_,y2 = np.loadtxt(r'C:\Users\fym12\PycharmProjects\ASIC_Test_Result_Saving\temp.csv', str,delimiter=',', usecols=(0,2), unpack=True,encoding='UTF-8')


mp.gcf().set_facecolor(np.ones(3) * 240/255)#设置背景色
fig, ax1 = plt.subplots() # 使用subplots()创建窗口
ax1.plot(dates, y1,'o-', c='orangered',label='y1', linewidth = 1) #绘制折线图像1,圆形点，标签，线宽
mp.legend(loc=2)
ax2 = ax1.twinx() # 创建第二个坐标轴
ax2.plot(dates, y2, 'o-', c='blue',label='y2', linewidth = 1) #同上
mp.legend(loc=1)

ax1.set_xlabel('时间', size=18)
ax1.set_ylabel('y1', size=18)
ax2.set_ylabel('y2', size=18)
mp.gcf().autofmt_xdate()#自动适应刻度线密度，包括x轴，y轴
plt.show()
