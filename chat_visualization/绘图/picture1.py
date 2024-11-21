
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
height=[2,3,4,5,6]
y1 = [0.017, 0.035, 0.034,0.043,0.049]
y11=[0.017+0.001,0.035+0.001,0.034+0.001,0.043+0.001,0.049+0.001]
y12=[0.017-0.001,0.035-0.001,0.034-0.001,0.043-0.001,0.049-0.001]
y2 = [0.020 ,0.028, 0.031,0.034,0.042]
y21=[0.020+0.001,0.028+0.001,0.031+0.001,0.034+0.001,0.042+0.001]
y22=[0.020-0.001,0.028-0.001,0.031-0.001,0.034-0.001,0.042-0.001]

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制第一条折线图并添加阴影效果
ax.plot(height, y1, linestyle='--', color='orange', marker='x', label='CSE', linewidth=2)
ax.fill_between(height, y12, y11, color='orange', alpha=0.3)

# 绘制第二条折线图并添加阴影效果
ax.plot(height, y2, linestyle='-', color='#ADD8E6', marker='o', label='LSEnet', linewidth=2)
ax.fill_between(height, y22, y21, color='#ADD8E6', alpha=0.3)

#显示每个点的数据
for i, txt in enumerate(y1):
    ax.annotate(txt, (height[i], y1[i]))
for i, txt in enumerate(y2):
    ax.annotate(txt, (height[i], y2[i]))

plt.xlabel('Height')
plt.ylabel('Time (seconds)')
# 添加图例
ax.legend()

# 显示图形
plt.show()
