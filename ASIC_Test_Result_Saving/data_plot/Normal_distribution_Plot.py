import matplotlib.pyplot as plt
import numpy as np
import math

from pandas import DataFrame


class curve_plot():
    def __init__(self):
        self

    # 正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
    def normfun(self,x, mu, sigma):
        pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))  # y_sig = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
        print(pdf)
        return pdf

    def plot_Nor_Distribution(self, data, min, max,test_case,test_configuration):

        u = 0  # 均值μ
        data_u=DataFrame(data)
        data_men=data_u.mean()
        data_men=data_men[0]
        data_sig=data_u.std()
        data_sig=data_sig[0]
        min_offset=min+data_men-(max+min)/2
        max_offset=max+data_men-(max+min)/2
        #u01 = -2
        # sig = math.sqrt(0.2)  # 标准差δ
        sig = 1

        # samples=[154,156,149,148,150,151]
        # samples = np.random.normal(100, 200, size=100)
        # plt.hist(samples, bins=100, normed=True, histtype='stepfilled', label='bins=100')

        x_1 = np.linspace(min, max, 50)                        #np.linspace(start,end,num)start代表起始的值，end表示结束的值，num表示在这个区间里生成数字的个数，生成的数组是等间隔生成的
        x_2=np.linspace(min_offset,max_offset,50)
        x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
        data_x = np.linspace(data_men - 3 * data_sig, data_men + 3 * data_sig, 50)
        y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
        y_sig_data = np.exp(-(data_x - data_men) ** 2 / (2 * data_sig ** 2)) / (math.sqrt(2 * math.pi) * data_sig)
        print(x)
        print("=" * 20)
        print(y_sig)
        #plt.plot(x_1, y_sig, "r-", linewidth=2)
        #plt.hist(x=data, bins=10)
        #plt2=plt.twinx()
        plt.figure(figsize=(12, 6))
        plt.ylabel('DUT Quantity')
        plt.xlabel('Test Result')
        if (max - min) > 100:
            hist_bins = 1
            hist_width = 100
        else:
            if (max - min > 20):
                hist_bins = 5
                hist_width = 0.5
            else:
                hist_bins = 5
                hist_width = 0.1
        plt.hist(x=data, bins=hist_bins, rwidth=hist_width, color='hotpink')
        plt.title('Test Case: %s :%s \n Standard σ=1 \n Test Result σ=%.8f  total quantity=%s ' % (test_case, test_configuration,data_sig,len(data)))
        plt2=plt.twinx()
        #plt.ylabel()
        plt2.plot(x_1, y_sig, "r-", linewidth=2,label='Standard Normal Distribution')                         #x_1 actual x axis vale for stand
        plt2.plot(x_2, y_sig_data, "b-", linewidth=2,label='Test Result Distribution')                        #x_2 DUT result for distribution,x_2 is offset for x_1
        #plt2.set_ylabel('y2',size=18)
        plt.legend()                                                                                          #plot assigned x&y label
        plt.show()

    def plot_historm(self, data, min, max, test_case,test_configuration):
        x=[min,max]
        y=[120,120]
        bar_width=(max-min)/200
        plt.figure(figsize=(10, 6))
        plt.ylabel('DUT Quantity')
        plt.xlabel('Test_Result')
        plt.title('Test Case: %s :%s \n total quantity=%s'%(test_case,test_configuration,len(data)))
        if (max-min)>100:
            hist_bins=1
            hist_width=100
        else:
            if (max-min>5):
                hist_bins=5
                hist_width=0.5
            else:
                hist_bins = 5
                hist_width = 0.1

        plt.hist(x=data, bins=hist_bins, rwidth=hist_width, color='hotpink',label="Test Result Distribution")
        plt.bar(x,y,width=bar_width,label="spec")
        plt.legend()
        plt.show()
        #plt.title('Commute Times for 1,000 Commuters')
        #plt.xlabel('Counts')
        #plt.ylabel('Commute Time')
        #plt.grid(axis='y', alpha=0.75)

        #plt2 = plt.twinx()
        #plt2.plot(x_1, y_sig, "r-", linewidth=2)
        #plt.grid(True)
        #plt.hist(x=data,bins=10, rwidth=10, color='#607c8e')
        '''
        mu = (max + min) / 2
        # mu = 32750
        sigma = 1
        # Python实现正态分布
        # 绘制正态分布概率密度函数
        #x = np.arange(min,max,1)
        x = np.linspace(mu - 3 * sigma, mu + 3 * sigma,50)  # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0),(在start和stop之间返回均匀间隔的数据)
        #y_sig = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
        y_sig = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
        # y_sig=normfun(x,mu,sigma)
        #plt.bar(x, y_sig, fc='b', linewidth=0.1)
        #plt.bar(5, data, fc='b',linewidth=1)
        plt.hist(x=data, bins=10)
        plt2 = plt.twinx()
        plt.plot(x, y_sig, "r-", linewidth=2)
        '''
        '''
        plt.vlines(mu, 0, np.exp(-(mu - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma), colors="c",
           linestyles="dashed")
        plt.vlines(mu + sigma, 0, np.exp(-(mu + sigma - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
           colors="k", linestyles="dotted")
        plt.vlines(mu - sigma, 0, np.exp(-(mu - sigma - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
           colors="k", linestyles="dotted")
        '''
        #plt.xticks([mu - sigma, mu, mu + sigma], ['μ-σ', 'μ', 'μ+σ'])
        #plt.xticks(5, x, fontsize='small')
        #plt.xlabel('')
        #plt.ylabel('Latent Trait')
        #plt.title('Normal Distribution: $\mu = %.2f, $sigma=%.2f' % (mu, sigma))
        #plt.grid(True)
        #plt.show()
