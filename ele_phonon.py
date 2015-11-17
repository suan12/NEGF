from environment import *
from gf import Lead, Coupling, System







lead0 = Lead(matrix([0]), matrix([-1]), matrix([0]))
lead1 = Lead(matrix([0]), matrix([-1]), matrix([0]))
lead2 = Lead(matrix([1]), matrix([-1]), matrix([1]))
lead3 = Lead(matrix([100]), matrix([-1]), matrix([100]))

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