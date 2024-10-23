import os
os.add_dll_directory("C:\\Users\\barna\\OneDrive\\Desktop\\UCL\\NPL Project\\.venv\\Lib\\site-packages\\igraph")

import numpy as np
import netket as nk
import jax
import scipy.sparse.linalg
import pandas
from scipy.sparse.linalg import eigsh



N = input("Enter the number of spin 1/2 particle in the chain:")
N=int(N)


#Creates a Hilbert space of N spin 1/2 particles. By defualt uses the z-spinor basis {+1.-1}
hi = nk.hilbert.Spin(1/2, N=N)

print("The Hilbert space has a basis of ",hi.size, " elements and a total of ", hi.n_states, " states.")

#Generates a random state in the hilbert space 'hi' in the z-spinor basis
print(hi.random_state(jax.random.key(0), 1))

#Hamiltonian (described by the LaTeX command bellow)

#H = -\Gamma\sum_{i}\sigma_i^{(x)} + V\sum_{i}\sigma_i^{(z)}\sigma_{i+1}^{(z)}, \quad i=0,1,...,L-1, \quad i=L=0

Gamma = -1
V=-1
H = sum([Gamma*nk.operator.spin.sigmax(hi,i) for i in range(N)]) #Independant components of the Hamiltonian, i=1,..,N-1
H = H + sum([V*nk.operator.spin.sigmaz(hi,i)*nk.operator.spin.sigmaz(hi,(i+1)%N) for i in range(N)]) #The interaction terms between sites i and i+1

sparse_H = H.to_sparse #Converting the Hamiltonian into a sparse matrix

eig_val, eig_vec = eigsh(sparse_H)

print("The lowest eigenvalue of the Hamiltonian, H, found with scipy's sparse matrix eigensolver is:", eig_val)
print("The eigenvector corresponding to thsi eigenvalue is:", eig_vec)
E_gs = eig_val[0]

