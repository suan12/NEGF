from environment import *
from phonon_GF import Phonon
from datetime import datetime
startTime = datetime.now()
omega = 0.5
n = 100
m = 10
out = 1
g = rand(n, m-7)
tmp = zeros((n, 3))
tmp.fill(out)
g = concatenate((tmp, g, tmp), axis=1)
g.fill(1)
f = rand(n-1, m-6)
tmp = zeros((n-1, 3))
tmp.fill(out)
f = concatenate((tmp, f, tmp), axis=1)
f.fill(1)
D_self = []
for i in range(m):
    D_self += [matrix(zeros((2*n,2*n)))]
D_couple = []
for i in range(m-1):
    D_couple += [matrix(zeros((2*n,2*n)))]
for j in range(m):
    for i in range(n):
        if i < n-1:
            D_self[j][2*i+1, 2*i+3] = -f[i, j]
            D_self[j][2*i+3, 2*i+1] = -f[i, j]
        if i == 0 or i == n-1:
            D_self[j][1, 1] = f[0, j]
            D_self[j][2*n-1, 2*n-1] = f[n-2, j]
        else:
            D_self[j][2*i + 1, 2*i + 1] = f[i-1, j] + f[i, j]
        if j == 0:
            D_self[j][2*i, 2*i] = g[i, j]
        elif j == m-1:
            D_self[j][2*i, 2*i] = g[i, j-1]
        else:
            D_self[j][2*i, 2*i] = g[i, j-1] + g[i, j]
for j in range(m-1):
    for i in range(n):
        D_couple[j][2*i, 2*i] = - g[i, j]
D = {'on_site': D_self[3: m-3], 'lead':{'l': [D_self[2], D_couple[1], D_self[1]], 'r': [D_self[m-3], D_couple[m-3], D_self[m-2]]},
     'couple': D_couple[3: m-4], 'lead_center':{'l': D_couple[2], 'r': D_couple[m-4]}}
test = Phonon(D, omega, 0.00000000000000000000000001)
test.cal_surface_GF(0.000001)
test.cal_self_energy()
test.cal_GF(flag='all')
test.cal_T()
print(test.T)
print(datetime.now() - startTime)