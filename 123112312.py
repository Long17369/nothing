# def quick_sort(lists,i,j):
# 	if i >= j:
# 		return list
# 	pivot = lists[i]
# 	low = i
# 	high = j
# 	while i < j:
# 		while i < j and lists[j] >= pivot:
# 			j -= 1
# 		lists[i]=lists[j]
# 		while i < j and lists[i] <=pivot:
# 			i += 1
# 		lists[j]=lists[i]
# 	lists[j] = pivot
# 	quick_sort(lists,low,i-1)
# 	quick_sort(lists,i+1,high)
# 	return lists

# if __name__=="__main__":
# 	lists=[30,24,5,58,18,36,12,42,39]
# 	print("：")
# 	for i in lists:
# 		print(i,end =" ")
# 	print("\n：")
# 	for i in quick_sort(lists,0,len(lists)-1):
# 		print(i,end=" ")


def quick_sort(alist, start, end):
	"""quick_sort"""
	if start >= end: 
		return
	mid = alist[start] 
	low = start  
	high = end  
	while low < high:
		while low < high and alist[high] >= mid:
			high -= 1
		alist[low] = alist[high]  
		while low < high and alist[low] < mid:
			low += 1
		alist[high] = alist[low]
	alist[low] = mid  
	quick_sort(alist, start, low - 1)  
	quick_sort(alist, low + 1, end)  



if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(alist, 0, len(alist) - 1)
	print(alist)
