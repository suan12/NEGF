from phonon_GF import Phonon
from environment import *
D = None
N = 100
omega_range =  linspace(0.00000001, 1, N)
T = zeros(N)
for i in range(N):
    omega = omega_range[i]
    system = Phonon(D, omega)
    system.cal_surface_GF()
    system.cal_self_energy()
    system.cal_GF(flag='all')
    system.cal_T()
    T[i] = system.T.real
print(omega_range)
print(T)
plt.plot(omega_range, T, 'ro-')
plt.show()