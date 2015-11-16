##
from environment import *
from gf import Lead, Coupling, System
##
f = 1.0
omega = 1.5
Dl00 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
Dl01 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
Dl11 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
Dr00 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
Dr01 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
Dr11 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
Dlcl = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
Dlcr = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])

D00 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D11 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D22 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D33 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D44 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D55 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D66 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D77 = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D01 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
D12 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
D23 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
D34 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
D45 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
D56 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
D67 = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
##
D = {'on_site': [D00, D11, D22, D33, D44, D55, D66, D77], 'lead':{'l': [Dl00, Dl01, Dl11], 'r': [Dr00, Dr01, Dr11]},
     'couple': [D01, D12, D23, D34, D45, D56, D67], 'lead_center':{'l': Dlcl, 'r': Dlcr}}
lead1 = Lead(Dl00, Dl01, Dl11)
lead2 = Lead(Dr00, Dr01, Dr11)

coupling1 = Coupling(lead1, 0, Dlcl)
coupling2 = Coupling(lead2, 7, Dlcr)
test = System(D, [coupling1, coupling2], 1.5, 2)
test.cal_diag_gf()
test.cal_T(0, 0)
test.cal_T(0, 1)
test.cal_T(1, 1)
gamma = matrix([[2,0,0,0],[0,0,0,0],[0,0,2,0],[0,0,0,0]])
print(gamma*test.gf[0][0].H*gamma*test.gf[0][0])
print('------------------')
print(test.gf[7][7])
print('------------------')
print(gamma*test.gf[0][7].H*gamma*test.gf[0][7])
print('------------------')
print(test.gf[0][7])
print(test.T)
##