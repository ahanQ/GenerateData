#coding:utf-8
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
	# 创建一个RandomWalk实例，并将其包含的点都绘制出来
	rw = RandomWalk()
	rw.fill_walk()

	# 设置绘图窗口的尺寸
	plt.figure(figsize = (10, 6))
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 15)

	# 突出起点烽终点
	plt.scatter(rw.x_values[0], rw.y_values[0], c = 'green', edgecolors = 'none', s = 100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()
	break

	# keep_running = input("Make another walk? (y/n): ")
	# if keep_running != 'y':
	# 	break