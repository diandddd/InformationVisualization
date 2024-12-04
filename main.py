import matplotlib.pyplot as plt

# 示例数据：年份和生育率数据（单位：生育率 - 每名女性平均生育的子女数量）
years = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

# 各地区的生育率数据（假设数据）
world_fertility = [4.70, 4.85, 3.73, 3.31, 2.72, 2.55, 2.30]
us_fertility = [3.65, 2.48, 1.84, 2.08, 2.06, 1.93, 1.64]
india_fertility = [5.92, 5.62, 4.78, 4.04, 3.35, 2.60, 2.05]

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制三条折线
plt.plot(years, world_fertility, marker='o', color='blue', linestyle='-', label='World')
plt.plot(years, us_fertility, marker='o', color='green', linestyle='-', label='United States')
plt.plot(years, india_fertility, marker='o', color='orange', linestyle='-', label='India')

# 添加标题和标签
plt.title('Fertility Rate (Children per Woman) from 1960 to 2020')
plt.xlabel('Year')
plt.ylabel('Fertility Rate (children per woman)')

# 添加网格
plt.grid(True)

# 设置X轴标签旋转角度
plt.xticks(years, rotation=45)

# 显示图例
plt.legend()

# 调整布局以避免重叠
plt.tight_layout()

# 显示图表
plt.show()
