# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:56:16 2020

@author: lenovo
"""

def Max(ls, direction, max0, x0): #输入列表，传递方向，现有的最高柱，最高柱坐标
	global Num_List 
	max_column = max(ls)	# 余下柱子最高柱
	x_column = []			# 余下柱子最高柱坐标
	for i in range(len(ls)):
		if ls[i] == max_column:
			x_column.append(i)	
	if direction == 'left':
		return max_column, min(x_column), (max0 - max_column) * x0
	else:
		return max_column, (max(x_column) + x0 + 1), (max0 - max_column) * (Num_List -  x0 - 1)

def ExtraWater(ColumnList, ls, direction, temp_max, temp_x):
	Extra_Water = 0
	while len(ls) != 0:
		temp_max, temp_x, temp_Extra_Water = Max(ls, direction, temp_max, temp_x)
		Extra_Water += temp_Extra_Water
		if direction == 'left':
			ls = ColumnList[:temp_x]
		else:
			ls = ColumnList[temp_x+1:]
	return Extra_Water

def CheckInfo(ls):
	if type(ls) == list:
		for i in range(len(ls)):
			if type(ls[i]) == int:
				pass
			else:
				print("输入列表中数据类型错误\n")
				return False
		return True
	else:
		print("输入数据非列表类型\n")
		return False

try:
	ColumnList = [1,3,0,4,1,0,1,3,2,1,2,1]
	#ColumnList = eval(input("请输入柱子数组，外侧使用[]，数据用,分隔："))
	if CheckInfo(ColumnList):
		X_Max_List = [] #记录最高柱子位置x坐标
		Num_List = len(ColumnList)
		Max_Column = max(ColumnList)
		Total_Water = Max_Column * Num_List

		for i in range(len(ColumnList)):
			if ColumnList[i] == Max_Column:
				X_Max_List.append(i)

		temp_x0_left = min(X_Max_List)
		temp_x0_right = max(X_Max_List)
		Extra_Water = ExtraWater(ColumnList, ColumnList[:temp_x0_left], 'left', Max_Column, temp_x0_left) + \
				ExtraWater(ColumnList, ColumnList[temp_x0_right+1:], 'right', Max_Column, temp_x0_right)

		Real_Water = Total_Water - Extra_Water - sum(ColumnList)

		print("一共拥有" + str(Real_Water) + "单位水\n")
except:
	print("发生错误\n")