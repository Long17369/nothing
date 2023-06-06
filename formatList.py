from dic import litter,num

class main():
	def __init__(self) -> None:
		self.intlist = self.intList
		self.formatstr = self.formatStr
		pass
	def intList(self,List:list,multiple:int = 0):
		n = len(List)
		if multiple == 0:
			multiple = n
		for i in range(n):
			List[i] = int(List[i]*multiple)
		return List
	def formatStr(self,words:str):
		re = []
		word = words.split('\n')
		for i in word:
			a = ' '
			for j in i:
				if i in litter:
					a += j
				elif i in num:
					pass
				else :
					a += j
			if a != '':
				re.append(a)
		return re

formatList = main()
formatstr = formatList.formatstr
intlist = formatList.intlist