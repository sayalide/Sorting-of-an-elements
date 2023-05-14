class quick:
	def __init__(P):
		P.value3 = []
	def insert(P, value):
		P.value3.append(value)
	def pprint(P):
		print '', P.value3
	def quicksort(P):
                qstart_time = time.time()
		P.quicksort1(0, len(P.value3) - 1)
		quicksorttime =time.time() - qstart_time
		return quicksorttime
	def quicksort1(P, l, r):
		if r-l+1 <= 3:
			P.quicksort2(l, r)
		else:	
			median = P.median_of_three(l, r)
			partition_of_array = P.divide_sort(l, r, median)
			P.quicksort1(l, partition_of_array-1)
			P.quicksort1(partition_of_array+1, r)
	

	def median_of_three(P, l, r):
		m = (l + r)/2
		if P.value3[l] > P.value3[m]:
			P.swap_sort(l, m)
		if P.value3[l] > P.value3[r]:
			P.swap_sort(l, r)
		if P.value3[m] > P.value3[r]:
			P.swap_sort(m, r)

		P.swap_sort(m, r - 1)
		return P.value3[r - 1]

	def swap_sort(P, a, b):
		P.value3[a], P.value3[b] = P.value3[b], P.value3[a]
	
	def divide_sort(P, l, r, divide_pivot):
		l1 = l
		r1 = r - 1
		while True:
			l1 += 1
			while P.value3[l1] < divide_pivot:
					l1 += 1
			r1 -= 1
			while P.value3[r1] > divide_pivot:
					r1 -= 1

			if l1 >= r1:	
				break	
			else:	
				P.swap_sort(l1, r1)
		P.swap_sort(l1, r - 1)
		return l1
	def quicksort2(P, l, r):
		if r-l+1 <= 1:
			return	
		if r-l+1 == 2:
			if P.value3[l] > P.value3[r]:
				P.swap_sort(l, r)
			return
		else:	
			if P.value3[l] > P.value3[r-1]:
				P.swap_sort(l, r-1)
			if P.value3[l] > P.value3[r]:
				P.swap_sort(l, r)
			if P.value3[r-1] > P.value3[r]:
				P.swap_sort(r-1, r)
