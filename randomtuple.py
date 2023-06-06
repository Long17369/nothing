from random import random


class mainfan():
	def __init__(self) -> None:
		self.list = self.randomlist
		self.listInt = self.randomlistInt
		pass
	def randomlist(self,count:int = 10) -> list:
		p = []
		for i in range (count):
			p.append(random())
		return p
	def randomlistInt(self,count:int = 10) -> list:
		p = self.randomlist(count)
		for i in range(count):
			p[i] = int(p[i]*count*10)
		return p

main = mainfan()
	# randomlist	-> list

class RandomS():
	def __init__(self) -> None:
		self.order=self.orderlist
		pass
	def orderlist(self,n):
		Order = main.list(n)
		return Order

randoms = RandomS()
	# orderlist		-> order