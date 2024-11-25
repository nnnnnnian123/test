#原题是头歌里面的题目，用于练习字典，字符串和绘图
#文件中有各个公司相应的股票数据，题目要求就是把这些数据以图像的形式画出来
#再加上import numpy就是数据处理三剑客了
import pandas as pd
import matplotlib.pyplot as plt
def draw():
    #里面存放着各公司股票数据
    files = ['AAPL.csv', 'GOOG.csv', 'MSFT.csv']
    colors = ['red', 'green', 'blue']
    labels = ['Apple', 'Google', 'Microsoft']
    #设定各个公司的曲线，同时设置曲线的相关性质
    for filel, color, label in zip(files, colors, labels):
        df = pd.read_csv(filel)
        df['Date'] = pd.to_datetime(df['Date'])
        dates = df['Date'].values
        opens = df['Open'].values
        plt.plot(dates, opens, color=color, label=label, linewidth=1.0)
    #其余设置，比如坐标轴，横坐标旋转45度，横纵坐标的标签，储存路径和展示
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.ylabel('Open')
    plt.savefig('data.png')
    plt.show()
#运行函数
draw()
