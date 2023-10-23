import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.font_manager import FontProperties

print("qqqq")
def prc(name,num,ylima,ylimb):
    ax = plt.subplot()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_position(('data',0))
    data = np.loadtxt(name,skiprows=3,usecols=1)
    time = np.loadtxt(name,skiprows=3,usecols=0)
    len_data = len(data)
    i=0
    arr=[]
    arrs= []
    while(i<len_data/60):
        arr.append(i*60)
        arrs.append(str(i))
        i=i+1
    ave_data = np.mean(data)
    ax.spines["bottom"].set_position(('data',ave_data))
    #ax.set_xticks(arr)
    #ax.set_xticklabels(arrs)
    #plt.scatter(time,data,s=2,c="black")
    #plt.plot(time,data,color="black")
    #plt.show()
    data1 = data[num:]
    time1 = time[:len_data-num]
    len1 = len_data-num
    i=0
    arr1=[]
    arrs1= []
    while(i<len1/60):
        arr1.append(i*60)
        arrs1.append(str(i))
        i=i+1
    ave_data1 = np.mean(data1)
    ax.spines["bottom"].set_position(('data',ave_data1))
    ax.set_xticks(arr1)
    ax.set_xticklabels(arrs1)
    plt.scatter(time1,data1,s=2,c="black")
    plt.plot(time1,data1,color="black")
    plt.ylim(ylima,ylimb)
    font = FontProperties(fname='c:\\Windows\\Fonts\\SIMSUN.TTC', size=12)
    plt.xlabel('时间（min）',fontproperties=font,labelpad=-10,x=1.04,rotation=0)
    plt.ylabel('温度（℃）',fontproperties=font,labelpad=-40,y=1.04,rotation=0)
    plt.show()
    plt.savefig("1.png")

prc("张相梓\张相梓\DTC-125-YOU.txt",1090,35,36)
#张相梓\张相梓\DTC-125-YOU.txt 为名称
#1090 从第1090个数据开始
#35 26 为y轴范围
