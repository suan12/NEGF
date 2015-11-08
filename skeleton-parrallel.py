from phonon_GF import Phonon
from environment import *
from jug import TaskGenerator
N = 100
omega_range =  linspace(0.001, 5, N)
D = None
@TaskGenerator
def cal_T(omega):
    system = Phonon(D, omega)
    system.cal_surface_GF()
    system.cal_self_energy()
    system.cal_GF(flag='all')
    system.cal_T()
    return system.T.real
T = [cal_T(omega) for omega in omega_range]