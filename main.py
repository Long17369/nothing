from randomtuple import main as ran
from sort import *
from random import random
from formatList import intlist,formatstr
from time import process_time


class Main():
	def __init__(self) -> None:
		pass
	def load(self,file:str):
		a = open(file,'r',)
		r = a.read()
		e, c = self.order(r)
		p = formatstr(r)
		a.close()
		return e, c
	def order(self,words:str):
		word = words.split('\n')
		e = [word[i].split(' ')[0] for i in range(int(len(word)))]
		c = [word[i].split(' ')[1] for i in range(int(len(word)))]
		return e, c
		...


main = Main()
load = main.load


if __name__ == '__main__':
	a = load('123.txt')
	for i in a:
		print (i,end=' ')
	print()