from environment import *
from gf import Lead, Coupling, System
'''
lead0 = Lead(matrix([0]), matrix([-1]), matrix([0]))
lead1 = Lead(matrix([0]), matrix([-1]), matrix([0]))
lead2 = Lead(matrix([1]), matrix([-1]), matrix([1]))
lead3 = Lead(matrix([1]), matrix([-1]), matrix([1]))

coupling0 = Coupling(lead0, 0, matrix([-1]))
coupling1 = Coupling(lead1, 0, matrix([-1]))
coupling2 = Coupling(lead2, 1, matrix([-1]))
coupling3 = Coupling(lead3, 1, matrix([-1]))

system = System({'on_site': [matrix([0]), matrix([1])], 'couple': [matrix([-1])]}, [coupling0, coupling1, coupling2, coupling3], 0, 1)

system.cal_diag_gf()
system.cal_T(0,1)
system.cal_T(0,2)
system.cal_T(0,3)
print(system.T)
'''
'''
N = 8
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
E_range = linspace(-2, 2, 500)
for E in E_range:
    system = System(D, couplings, E, 1)
    system.cal_diag_gf()
    system.cal_T(0, 1)
    T.append(system.T[0, 1])
plt.plot(E_range, T)
plt.show()
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
plt.plot(E_range, T)
plt.show()