import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import math


# a = pd.read_excel(r"C:\Users\周俊杰\Desktop\SXJM\A题\附件\c1.xlsx")
# print(a.iloc[:,4])
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# plt.plot(x, y)
# plt.xticks(rotation=45)  # 旋转x轴的刻度标签45度
# plt.show()


a=np.random.rand(2,4,3,5)
b=a.shape
c=a.max(axis=1)
d=c.shape
print(b,'\n',d,'\n',a,'\n','new:','\n',c)

f= 1
print(f)
