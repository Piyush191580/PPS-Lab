'''1.1.15. Write a Python program to perform multiplication of two matrices
10:41








Sample Test Cases
Test case 1
Enter·values·for·matrix·-·A⏎	
Number·of·rows,·m·=·2	
Number·of·columns,·n·=·2	
Entry·in·row:·1·column:·1⏎	
1	
Entry·in·row:·1·column:·2⏎	
2	
Entry·in·row:·2·column:·1⏎	
3	
Entry·in·row:·2·column:·2⏎	
4	
Enter·values·for·matrix·-·B⏎	
Number·of·rows,·m·=·2	
Number·of·columns,·n·=·2	
Entry·in·row:·1·column:·1⏎	
1	
Entry·in·row:·1·column:·2⏎	
2	
Entry·in·row:·2·column:·1⏎	
3	
Entry·in·row:·2·column:·2⏎	
4	
Matrix·-·A·=·[[1,·2],·[3,·4]]⏎	
Matrix·-·B·=·[[1,·2],·[3,·4]]⏎	
Matrix·-·A·*·Matrix-·B·=·[[7,·10],·[15,·22]]⏎	
Test case 2
Enter·values·for·matrix·-·A⏎	
Number·of·rows,·m·=·2	
Number·of·columns,·n·=·3	
Entry·in·row:·1·column:·1⏎	
1	
Entry·in·row:·1·column:·2⏎	
2	
Entry·in·row:·1·column:·3⏎	
3	
Entry·in·row:·2·column:·1⏎	
4	
Entry·in·row:·2·column:·2⏎	
5	
Entry·in·row:·2·column:·3⏎	
6	
Enter·values·for·matrix·-·B⏎	
Number·of·rows,·m·=·3	
Number·of·columns,·n·=·2	
Entry·in·row:·1·column:·1⏎	
1	
Entry·in·row:·1·column:·2⏎	
2	
Entry·in·row:·2·column:·1⏎	
3	
Entry·in·row:·2·column:·2⏎	
4	
Entry·in·row:·3·column:·1⏎	
5	
Entry·in·row:·3·column:·2⏎	
6	
Matrix·-·A·=·[[1,·2,·3],·[4,·5,·6]]⏎	
Matrix·-·B·=·[[1,·2],·[3,·4],·[5,·6]]⏎	
Matrix·-·A·*·Matrix-·B·=·[[22,·28],·[49,·64]]⏎	
Test case 3
Enter·values·for·matrix·-·A⏎	
Number·of·rows,·m·=·3	
Number·of·columns,·n·=·2	
Entry·in·row:·1·column:·1⏎	
1	
Entry·in·row:·1·column:·2⏎	
2	
Entry·in·row:·2·column:·1⏎	
3	
Entry·in·row:·2·column:·2⏎	
3	
Entry·in·row:·3·column:·1⏎	
2	
Entry·in·row:·3·column:·2⏎	
1	
Enter·values·for·matrix·-·B⏎	
Number·of·rows,·m·=·2	
Number·of·columns,·n·=·1	
Entry·in·row:·1·column:·1⏎	
1	
Entry·in·row:·2·column:·1⏎	
2	
Matrix·-·A·=·[[1,·2],·[3,·3],·[2,·1]]⏎	
Matrix·-·B·=·[[1],·[2]]⏎	
Matrix·-·A·*·Matrix-·B·=·[[5],·[9],·[4]]⏎'''


def matmult(A, B):
	rows_A = len(A)
	cols_A = len(A[0])

	rows_B = len(B)
	cols_B = len(B[0])

	if cols_A != rows_B :
		print("Cannot multiply the two matrices. Incorrect dimensions.")
		return None

	result = []
	for i in range(rows_A):
		row=[]
		for j in range(cols_B):
			row.append(0)
		result.append(row)

	for i in range(rows_A):
		for j in range(cols_B):
			for k in range(cols_A):
				result[i][j]+=A[i][k]*B[k][j]
	return result

def readmatrix(name=''):
	print(f"Enter values for {name}")
	rows=int(input("Number of rows, m = "))
	cols=int(input("Number of columns, n = "))

	matrix = []

	for i in range(rows):
		row=[]
		for j in range(cols):
			print(f"Entry in row: {i+1} column: {j+1}")
			value= int(input())
			row.append(value)
		matrix.append(row)

	return matrix 

matrixa=readmatrix('matrix - A')
matrixb=readmatrix('matrix - B')
print("Matrix - A =",matrixa)
print("Matrix - B =",matrixb)
print("Matrix - A * Matrix- B =",matmult(matrixa,matrixb))
