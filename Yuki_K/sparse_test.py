from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

l = [[1, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 3, 0],
     [0, 0, 0, 4]]

csr = csr_matrix(l)
csc = csc_matrix(l)
coo = coo_matrix(l)
lil = lil_matrix(l)

print(csr.toarray())
print(csr.getrow(0))
#   (0, 0)  1

lil[:,0]=20
lil[0,:]=20
print(lil.toarray())

