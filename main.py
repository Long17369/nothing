from randomtuple import main as ran
from sort import *
from random import random
from formatList import intlist,formatstr
from time import process_time


class Main():
	def __init__(self) -> None:
		pass
	def load(self,file:str):
		a = open(file,'r',encoding='UTF-8')
		r = a.read()
		e, c = self.order(r)
		p = formatstr(r)
		a.close()
		return e, c
	def order(self,words:str):
		word = words.split('\n')
		e, c = [], []
		for i in word:
			j = i.split(' ')
			e.append(j[0])
			c.append(j[1])
		return e, c
	def sort(self, l1 :list, l2 :list, l1_sort :list, l2_sort :list):
		ll1, ll2, ll3= len(l1), len(l2), len(l1_sort)
		if ll1 != ll2 or ll1 != ll3:
			print('Error:无法排序')
			return 
		for i in l1_sort:
			for j in range(ll3):
				if i == l1[j]:
					l2_sort.append(l2[j])
					break


main = Main()
load = main.load
sort = main.sort


if __name__ == '__main__':
	e, c = load('123.txt')
	e_sort = e
	quick(e_sort)
	c_sort = c
	sort(e, c, e_sort, c_sort)
	print(e_sort)