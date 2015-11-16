from environment import *


class Phonon(object):

    def __init__(self, D, omega, delta=0.000001):

        """
        D should be a dictionary, the format is:
        D = {'on_site': [D00, D11, D22, D33 ...], 'lead':{'l': [Dl00, Dl01, Dl11], 'r': [Dr00, Dr01, Dr11]},
        'couple': [D01, D12, D23 ...], 'lead_center':{'l': Dlcl, 'r': Dlcr}}
        """
        self.D = D
        self.omega = omega
        # size of primitive cells in left/right lead and center area
        self.size = {'l': D['lead']['l'][0].shape[0], 'r': D['lead']['r'][0].shape[0],
                     'c': D['on_site'][0].shape[0]}
        # the number of cells in center area
        self.length = len(D['on_site'])
        # self.GF is used to store green's function of any type
        self.GF = {'surface': {'l': None, 'r': None},
                   'center': [0]*self.length, 'through': None}
        # store self_energy of leads
        self.self_energy = {'l': None, 'r': None}
        # self.delta is used in (omega + i delta)^2 to calculate green's function
        self.delta = delta
        # store transmission probability
        self.T = None

    def M(self, i, j):
        if i == j:
            return (self.omega + 1j*self.delta)**2*eye(self.size['c']) - self.D['on_site'][i]
        if i + 1 == j:
            return -self.D['couple'][i]
        if i == j + 1:
            return -self.D['couple'][j]

    def cal_surface_GF(self, epsilon=0.000001):
        """
        calculate surface green's function
        """
        omega = self.omega
        for lead in ('l', 'r'):
            I = eye(self.size[lead])
            Ws = ((omega + 1j*self.delta)**2)*I - self.D['lead'][lead][0]
            Wb = ((omega + 1j*self.delta)**2)*I - self.D['lead'][lead][2]
            tau1 = self.D['lead'][lead][1]
            tau2 = tau1.T
            while abs(tau1).max() > epsilon:
                Wb_I = Wb.I
                Ws = Ws - tau1*Wb_I*tau2
                Wb = Wb - tau1*Wb_I*tau2 - tau2*Wb_I*tau1
                tau1 = tau1*Wb_I*tau1
                tau2 = tau1.T
            self.GF['surface'][lead] = Ws.I

    def cal_self_energy(self):
        """
        calculate self energy. Surface green's function must be calculated first
        """
        for lead in ('l', 'r'):
            self.self_energy[lead] = \
                self.D['lead_center'][lead]*self.GF['surface'][lead]*self.D['lead_center'][lead].T

    def cal_GF(self, flag = 'minimal'):
        """
        calculate green's function for center area. Self energy of leads must be calculated first
        :param flag: minimal: calculate only G_NN, 'center': calculate all G_ii, 'through': calculate G_1N,
        'all': all green's function
        """
        from operator import mul
        length = self.length
        g = [0]*length
        # forward iterating
        if length == 1:
            g[0] = (self.M(0, 0) - self.self_energy['l'] - self.self_energy['r']).I
        else:
            g[0] = (self.M(0, 0) - self.self_energy['l']).I
            for j in range(1, length - 1):
                g[j] = (self.M(j, j) -
                        self.M(j, j-1)*g[j-1]*self.M(j-1, j)).I
            g[self.length - 1] = (
                self.M(length - 1, length - 1) - self.self_energy['r'] -
                self.M(length - 1, length - 2)*g[length - 2]*self.M(length - 2, length - 1)
                              ).I
        G = self.GF['center']
        G[self.length - 1] = g[self.length - 1]
        # calculate more green's function according to the flag
        # backward iterating
        if flag == 'center' or flag == 'all':
            for j in list(range(self.length - 1))[::-1]:
                G[j] = g[j] + g[j]*self.M(j, j+1)*G[j+1]*self.M(j+1, j)*g[j]
        if flag == 'through' or flag == 'all':
            self.GF['through'] = reduce(mul, [g[j]*-self.M(j, j+1) for j in range(length - 1)], 1)*g[self.length - 1]

    def cal_T(self):
        """
        calculating transmission probability
        """
        gamma_r = 1j*(self.self_energy['r'] - self.self_energy['r'].H)
        gamma_l = 1j*(self.self_energy['l'] - self.self_energy['l'].H)
        self.T = trace(gamma_r*self.GF['through'].H*gamma_l*self.GF['through'])



