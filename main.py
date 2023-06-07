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

	def write(self,l1 : list, l2 : list):
		w = open('file.txt','w',encoding='UTF-8')
		for i in range(len(l1)):
			w.write(l1[i] + ' ' + l2[i] + '\n')

	def firstLoad(self, file):
		e, c = load(file)
		e_sort = [i for i in e]
		quick(e_sort)
		c_sort = []
		self.reset()
		sort(e, c, e_sort, c_sort)
		write(e_sort,c_sort)

	def reset(self, name:str='file'):
		reset = open(name,'a+',encoding='UTF-8')
		reset.truncate(0)
		reset.close()


main = Main()
load = main.load
sort = main.sort
write = main.write


if __name__ == '__main__':
	...