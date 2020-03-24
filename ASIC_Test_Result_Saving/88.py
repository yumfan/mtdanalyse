    # Python实现正态分布
    import np
    import matplotlib.pyplot as plt
    import math
    # 绘制正态分布概率密度函数
    u = 0   # 均值μ
    u01 = -2
    sig = math.sqrt(0.2)  # 标准差δ
    sig01 = math.sqrt(1)
    sig02 = math.sqrt(5)
    sig_u01 = math.sqrt(0.5)
    x = np.linspace(u - 3*sig, u + 3*sig, 50)
    x_01 = np.linspace(u - 6 * sig, u + 6 * sig, 50)
    x_02 = np.linspace(u - 10 * sig, u + 10 * sig, 50)
    x_u01 = np.linspace(u - 10 * sig, u + 1 * sig, 50)
    y_sig = np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig)
    y_sig01 = np.exp(-(x_01 - u) ** 2 /(2* sig01 **2))/(math.sqrt(2*math.pi)*sig01)
    y_sig02 = np.exp(-(x_02 - u) ** 2 / (2 * sig02 ** 2)) / (math.sqrt(2 * math.pi) * sig02)
    y_sig_u01 = np.exp(-(x_u01 - u01) ** 2 / (2 * sig_u01 ** 2)) / (math.sqrt(2 * math.pi) * sig_u01)
    plt.plot(x, y_sig, "r-", linewidth=2)
    plt.plot(x_01, y_sig01, "g-", linewidth=2)
    plt.plot(x_02, y_sig02, "b-", linewidth=2)
    plt.plot(x_u01, y_sig_u01, "m-", linewidth=2)
    # plt.plot(x, y, 'r-', x, y, 'go', linewidth=2,markersize=8)
    plt.grid(True)
    plt.show()
