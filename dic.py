class Main():
	def __init__(self) -> None:
		pass
	def litterDic(self):
		a = 'a'
		dic = []
		for i in range(26):
			dic.append(a)
			a = chr(ord(a)+1)
		return dic
	def numberDic(self,n:int = 10):
		a = 1
		dic = []
		for i in range(n):
			dic.append(str(a))
			a += 1
		return dic


Dic = Main()
litter = Dic.litterDic()
nums = Dic.numberDic
num = nums()