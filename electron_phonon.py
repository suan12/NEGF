from environment import *
from gf import Lead, Coupling, System
#ele-phonon coupling
'''
N = 10
lam = 0.5
t = 1
t0 = 0.2
couplings = []
D = {'on_site': [], 'couple': []}
for i in range(N):
    for j in range(2):
        couplings.append(Coupling(Lead(matrix([i]), matrix([-t]), matrix([i])), i, matrix([-t0])))
    D['on_site'].append(matrix([i]))
    if i == 0:
        continue
    D['couple'].append(matrix([sqrt(i)*lam]))
T = []
E_range = linspace(-2, 2, 1000)
for E in E_range:
    system = System(D, couplings, E, 1)
    system.cal_diag_gf()
    [system.cal_T(0, i) for i in [1, 3, 5, 7, 9, 11, 13, 15]]
    T.append(sum(system.T[0, i] for i in [1, 3, 5, 7, 9, 11, 13, 15]))
plt.plot(E_range, T)
plt.show()
'''
#ele-phonon coupling, using matrix
'''
lam = 0.5
t = 1
t0 = 0.2
couplings = []
couplings.append(Coupling(Lead(matrix([0]), matrix([-t]), matrix([0])), 0, matrix([-t0])))
couplings.append(Coupling(Lead(matrix([0]), matrix([-t]), matrix([0])), 0, matrix([-t0])))
couplings.append(Coupling(Lead(matrix([[1, 0], [0, 2]]), matrix([[-t, 0], [0, -t]]), matrix([[1, 0], [0, 2]])), 1, matrix([[-t0, 0],[0,-t0]])))
couplings.append(Coupling(Lead(matrix([[1, 0], [0, 2]]), matrix([[-t, 0], [0, -t]]), matrix([[1, 0], [0, 2]])), 1, matrix([[-t0, 0],[0,-t0]])))
couplings.append(Coupling(Lead(matrix([[3, 0], [0, 4]]), matrix([[-t, 0], [0, -t]]), matrix([[3, 0], [0, 4]])), 2, matrix([[-t0, 0],[0,-t0]])))
couplings.append(Coupling(Lead(matrix([[3, 0], [0, 4]]), matrix([[-t, 0], [0, -t]]), matrix([[3, 0], [0, 4]])), 2, matrix([[-t0, 0],[0,-t0]])))
couplings.append(Coupling(Lead(matrix([[5, 0], [0, 6]]), matrix([[-t, 0], [0, -t]]), matrix([[5, 0], [0, 6]])), 3, matrix([[-t0, 0],[0,-t0]])))
couplings.append(Coupling(Lead(matrix([[5, 0], [0, 6]]), matrix([[-t, 0], [0, -t]]), matrix([[5, 0], [0, 6]])), 3, matrix([[-t0, 0],[0,-t0]])))
couplings.append(Coupling(Lead(matrix([7]), matrix([-t]), matrix([7])), 4, matrix([-t0])))
couplings.append(Coupling(Lead(matrix([7]), matrix([-t]), matrix([7])), 4, matrix([-t0])))
D = {'on_site': [matrix([0]), matrix([[1, sqrt(2)*lam], [sqrt(2)*lam, 2]]), matrix([[3, 2*lam], [2*lam, 4]]), matrix([[5, sqrt(6)*lam], [sqrt(6)*lam, 6]]), matrix([7])],
     'couple': [matrix([[lam, 0]]), matrix([[0, 0], [sqrt(3)*lam, 0]]), matrix([[0, 0], [sqrt(5)*lam, 0]]), matrix([[sqrt(7)*lam], [0]])]}
T = []
E_range = linspace(-2, 2, 500)
for E in E_range:
    system = System(D, couplings, E, 1)
    system.cal_diag_gf()
    system.cal_T(0, 1)
    system.cal_T(0, 3)
    system.cal_T(0, 5)
    system.cal_T(0, 7)
    system.cal_T(0, 9)
    T.append(system.T[0, 1]+system.T[0, 3]+system.T[0, 5]+system.T[0, 7]+system.T[0, 9])
plt.plot(E_range, T, 'o-')
plt.show()
'''
#weak coupling blockade
'''
N = 1
t = 1.0
t0 = 0.5
couplings = []
D = {'on_site': [], 'couple': []}
couplings.append(Coupling(Lead(matrix([0.]), matrix([-t]), matrix([0.])), 0, matrix([-t])))
couplings.append(Coupling(Lead(matrix([0.]), matrix([-t]), matrix([0.])), 4, matrix([-t])))
D['on_site'].append(matrix([0.]))
D['on_site'].append(matrix([0.]))
D['on_site'].append(matrix([1]))
D['on_site'].append(matrix([0.]))
D['on_site'].append(matrix([0.]))
D['couple'].append(matrix([-t]))
D['couple'].append(matrix([-t0]))
D['couple'].append(matrix([-t0]))
D['couple'].append(matrix([-t]))
T = []
E_range = linspace(0.5, 1.5, 1000)
for E in E_range:
    system = System(D, couplings, E, 1., 0.000000000000000001, 0.000000000000000001)
    system.cal_diag_gf()
    system.cal_T(0, 1)
    T.append(system.T[0, 1])
plt.plot(E_range, T, 'o-')
plt.show()
'''
#weak coupling pedestrian one line
'''
t = 1
t0 = 0.2
couplings = []
D = {'on_site': [], 'couple': []}
couplings.append(Coupling(Lead(matrix([0]), matrix([-t]), matrix([0])), 0, matrix([-t])))
couplings.append(Coupling(Lead(matrix([0]), matrix([-t]), matrix([0])), 4, matrix([-t])))
D['on_site'].append(matrix([0]))
D['on_site'].append(matrix([0]))
D['on_site'].append(matrix([[0, -t0], [-t0, 0]]))
D['on_site'].append(matrix([0]))
D['on_site'].append(matrix([0]))
D['couple'].append(matrix([-t]))
D['couple'].append(matrix([[-t, 0]]))
D['couple'].append(matrix([[-t], [0]]))
D['couple'].append(matrix([-t]))
T = []
E_range = linspace(-2, 1.99, 1000)
for E in E_range:
    system = System(D, couplings, E, 1)
    system.cal_diag_gf()
    system.cal_T(0, 1)
    T.append(system.T[0, 1])
plt.plot(E_range, T, 'o-')
plt.show()
'''
# weak coupling pedestrian several dangling atoms and several line
'''
N = 2
M = 3
t = 1
t0 = 0.2
couplings = []
D_couple = matrix(zeros((N+M, N)))
for i in range(N):
    D_couple[i+M,i] = -t
D_on_site = matrix(zeros((N+M, N+M)))
for i in range(N+M-1):
    if i == M-1:
        D_on_site[i+1, i] = -t0
        D_on_site[i, i+1] = -t0
    else:
        D_on_site[i+1, i] = -t
        D_on_site[i, i+1] = -t
D = {'on_site': [D_on_site], 'couple': []}
couplings.append(Coupling(Lead(matrix(zeros((N, N))), matrix(eye(N))*-t, matrix(zeros((N, N)))), 0, D_couple))
couplings.append(Coupling(Lead(matrix(zeros((N, N))), matrix(eye(N))*-t, matrix(zeros((N, N)))), 0, D_couple))
T = []
E_range = linspace(-2, 2, 1000)
for E in E_range:
    system = System(D, couplings, E, 1)
    system.cal_diag_gf()
    system.cal_T(0, 1)
    T.append(system.T[0, 1])
plt.plot(E_range, T, 'o-')
plt.show()
'''