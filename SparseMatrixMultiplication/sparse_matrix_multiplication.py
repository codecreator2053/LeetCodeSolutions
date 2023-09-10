#A->m*n, B->n*l, O(mnl), O(1)
class Solution:
	def multiply(self, A, B):

		def mul_row_col(m ,n):
			sum_ = 0
			for j in range(len(B)):
					sum_ += A[m][j] * B[j][n]
			return sum_



		A_row = len(A)
		A_col = B_row = len(A[0])
		B_col = len(B[0])
		res  = []
		print(A_row, A_col, B_row, B_col)
		for i in range(A_row):
			row = []
			for j in range(B_col):
				row.append(mul_row_col(i, j))
			res.append(row)
		return  res



#A->m*n, B->n*l, O(mnl), O(1)
class Solution2:
	def multiply(self, A, B):
		A_row = len(A)
		A_col = B_row = len(A[0])
		B_col = len(B[0])
		res  = []
		for i in range(A_row):
			row = []
			for j in range(B_col):
				sum_ = 0
				for k in range(len(B)):
					sum_ += A[i][k] * B[k][j]
				row.append(sum_)
			res.append(row)
		return res




#A->m*n, B->n*l, O(mnl), O(1), optimised with condition checking
class Solution3:
	def multiply(self, A, B):
		A_row = len(A)
		A_col = B_row = len(A[0])
		B_col = len(B[0])
		res = [[0 for _ in range(B_col)] for _ in range(A_row)]
		for i in range(A_row):
			for j in range(A_col):
				if A[i][j]!=0:
					for k in range(B_col):
						res[i][k] += A[i][j] * B[j][k]
		return res



class Solution3:
	def multiply(self, A, B):
		A_row = len(A)
		A_col = B_row = len(A[0])
		B_col = len(B[0])
		res = [[0 for _ in range(B_col)] for _ in range(A_row)]

		map = {}
		for j in range(B_row):
			map[j] = {}
			for k in range(B_col):
				if B[j][k]!=0:
					map[j][k] = B[j][k]


		for i in range(A_row):
			for j in range(A_col):
				if A[i][j]!=0:
					for k in map[j].keys():
						res[i][k] += A[i][j] * B[j][k]
		return res


A=[[1, 0, 0],[0, 0, 2]]
B = [[0, 2],[1, -1],[0, 0]]
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
soln = Solution3()
print(soln.multiply(A, B))




