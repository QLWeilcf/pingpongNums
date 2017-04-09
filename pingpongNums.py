#coding=UTF-8

"""
乒乓序列从1开始计数，并且始终向上或向下计数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
定义一个函数 pingpong ，传入一个正整数参数 n ，返回第 n 个乒乓数
2017-4-9 14:35:10
函数如下：

"""
def pingpong(n):
	start = 1 #明面上的数；
	rank = 1 #下标
	op=1#操作数  奇数:+   偶数: -
	if n<=0:
		print("input error")
	else:
		while (rank<n):
			if (rank%7==0 or ('7' in str(rank))):
				op+=1

			if (op%2==0): #转向的情况
				start-=1
			else:
				start+=1
			rank += 1
		print(start)


def pingpongZero(n,k):
	start = 1 #明面上的数；
	rank = 1 #下标
	kstr=str(k)
	op=1#操作数  奇数:+   偶数: -
	if n<=0:
		print("input error")
	else:
		while (rank<n):
			if (rank%k==0 or (kstr in str(rank))):
				op+=1

			if (op%2==0):
				start-=1
			else:
				start+=1
			rank += 1
		print(start)


def pingpongOne(rk):
	#返回第几个转向的数，从1开始计数
	start = 1 #明面上的数；
	rank = 1 #下标
	count=0 #和n比较的数
	op=1#  奇数:+   偶数: -
	if rk<=0:
		print("input error")
	else:
		while (count<=rk):
			if count==(rk):
				print('[*'+str(start)+'*]',end=' ')
				break

			if (rark%7==0 or ('7' in str(rark))):
				print('[' + str(start) + ']', end=' ')
				op+=1
				count += 1
				if count==(rk):
					break

			else:
				print(start,end=' ')


			if (op%2==0):
				start-=1
			else:
				start+=1
			rark += 1


# for i in [2,7,8,21,100]:
	# pingpong(i)

#pingpongZero(100,9)

#pingpongOne(28)
#for i in [7,8,21,100]:
	#pingpong(i)

'''
1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4]

1:7
2:0
3:3
4:-1
5:5
6:4
'''
