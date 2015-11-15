from environment import *
from gf import *
f = 1.0
omega = 1.5
D00 = matrix([2*f])
D11 = matrix([2*f])
D22 = matrix([2*f])
D33 = matrix([2*f])
D44 = matrix([f])
D55 = matrix([2*f])
D66 = matrix([2*f])
D77 = matrix([2*f])
Dl00 = matrix([2*f])
Dl01 = matrix([-f])
Dl11 = matrix([2*f])
Dr00 = matrix([2*f])
Dr01 = matrix([-f])
Dr11 = matrix([2*f])
D01 = matrix([-f])
D12 = matrix([-f])
D23 = matrix([-f])
D34 = matrix([-f])
D45 = matrix([-f])
D56 = matrix([-f])
D67 = matrix([-f])
Dlcl = matrix([-f])
Dlcr = matrix([-f])
D = {'on_site': [D00, D11, D22, D33, D44, D55, D66, D77], 'couple': [D01, D12, D23, D34, D45, D56, D67]}
lead1 = Lead(Dl00, Dl01, Dl11)
lead2 = Lead(Dr00, Dr01, Dr11)
coupling1 = Coupling(lead1, 0, Dlcl)
coupling2 = Coupling(lead2, 7, Dlcr)
test = System(D, [coupling1, coupling2], 1.5, 2)
test.cal_gf()
test.cal_T(0,1)
print(test.T)