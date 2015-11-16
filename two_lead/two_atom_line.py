##
from environment import *
from two_lead.phonon_GF import Phonon
f = 1.0
omega = 1.5
N = 100
D_self = matrix([[2*f, 0, 0, 0], [0, f, 0, -f], [0, 0, 2*f, 0], [0, -f, 0, f]])
D_couple = matrix([[-f, 0, 0, 0], [0, 0, 0, 0], [0, 0, -f, 0], [0, 0, 0, 0]])
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

# D = {'on_site': [D_self for i in range(N)], 'lead':{'l': [Dl00, Dl01, Dl11], 'r': [Dr00, Dr01, Dr11]},
#       'couple': [D_couple for i in range(N-1)], 'lead_center':{'l': Dlcl, 'r': Dlcr}}
D = {'on_site': [D00, D11, D22, D33, D44, D55, D66, D77], 'lead':{'l': [Dl00, Dl01, Dl11], 'r': [Dr00, Dr01, Dr11]},
     'couple': [D01, D12, D23, D34, D45, D56, D67], 'lead_center':{'l': Dlcl, 'r': Dlcr}}
# D = {'on_site': [D00, D11], 'lead':{'l': [Dl00, Dl01, Dl11], 'r': [Dr00, Dr01, Dr11]},
#      'couple': [D01], 'lead_center':{'l': Dlcl, 'r': Dlcr}}
test = Phonon(D, omega, 0.0000000000000001)
test.cal_surface_GF(0.000001)
test.cal_self_energy()
test.cal_GF(flag='all')
test.cal_T()
print(test.GF['center'][0])
print('--------------------------------------')
print(test.GF['center'][7])
print('--------------------------------------')
print(test.T)
##