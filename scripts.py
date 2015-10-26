from environment import *

# ATTENTION: Non-convergence may appear
f = 1.0
omega = 1.5
for N in range(200,4000,200):
    print(N)
    delta = 0.00000000001
    D = matrix(zeros((N, N)))
    I = matrix(eye(N))
    for i in range(1, N-1):
        D[i,i] = 2*f
    D[0, 0] = 2*f
    D[N-1, N-1] = 2*f
    for i in range(0, N-1):
        D[i, i+1] = -f
        D[i+1, i] = -f
    W = (omega + 1j*delta)**2*I-D
    print(W.I[0,0])
    print(omega)
#print(D)
#print(W)