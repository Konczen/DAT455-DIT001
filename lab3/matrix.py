import sys

def transpose(m):
	if not m:
		return m
	else:
		list1=[]
		for i in range(len(m[0])):
			list2=[]
			for j in range (len(m)):
				value=m[j][i]
				list2.append(value)
			list1.append(list2)
		return list1

def powers(inpList,p1,p2):
	m1=[]
	for j in inpList:
		m2=[]
		for i in range(p1,p2+1):
			result=j**i
			m2.append(result)
		m1.append(m2)
	return m1

def matmul(A, B):
	if not A:
		return A
	else:
		rowsA = len(A)
		colsA = len(A[0])
		colsB = len(B[0])

		C = [[0 for x in range(colsB)] for y in range(rowsA)]

		for i in range(rowsA):	
			for j in range(colsB):	
				for ii in range(colsA):	
					C[i][j] += A[i][ii] * B[ii][j]
	return C

def invert(matrice):
    a = matrice[0][0]
    b = matrice[0][1]
    c = matrice[1][0]
    d = matrice[1][1]
    det = a*d - b*c

    list = [[0,0],[0,0]]
    list = [[d/det,-b/det],[-c/det, a/det]]
    return list

def loadtxt(f):
    file = open(f, "r")

    data_list = file.read().split()
    data_list = list(map(float, data_list))

    mx = []
    while data_list != []:
        mx.append(data_list[:2])
        data_list = data_list[2:]
    return mx

