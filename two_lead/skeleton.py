from datetime import datetime

from environment import *
from two_lead.one_atom_line import D
from two_lead.phonon_GF import Phonon

N = 500
omega_range = linspace(0.00000001, 3, N)
T = zeros(N)
start_time = datetime.now()
for i in range(N):
    omega = omega_range[i]
    system = Phonon(D, omega)
    system.cal_surface_GF()
    system.cal_self_energy()
    system.cal_GF(flag='all')
    system.cal_T()
    T[i] = system.T.real
print(datetime.now() - start_time)
plt.plot(omega_range, T, 'ro-')
plt.show()