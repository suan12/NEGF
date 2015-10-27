from environment import *


class Phonon(object):

    def __init__(self, D, omega_list, delta = 0.0001):

        """
        D should be a dictionary, the format is:
        D = {'on_site': [D00, D11, D22, D33 ...], 'lead':{'l': [Dl00, Dl01, Dl11], 'r': [Dr00, Dr01, Dr11],
        'couple': [D01, D12, D23 ...], 'lead_center':{'l': Dlcl, 'r': Dlcr}}
        omega_list is a list of frequencies to calculate
        """
        self.D = D
        self.omega_list = omega_list
        self.size = {'l': D['lead']['l'][0].shape[0], 'r': D['D_lead']['r'][0].shape[0],
                     'c': D['lead']['c'][0].shape[0]}
        self.length = len(D['on_site'])
        self.GF = {'surface': {'l': zeros(len(omega_list)).tolist(), 'r': zeros(len(omega_list)).tolist()},
                   'center': zeros((len(omega_list), self.length)).tolist()}
        self.self_energy = {'l': zeros(len(omega_list)).tolist(), 'r': zeros(len(omega_list)).tolist()}
        self.delta = delta

    def cal_surface_GF(self, epsilon=0.0001):
        """
        calculate surface green's function
        """
        for i in range(len(self.omega_list)):
            omega = self.omega_list[i]
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
                self.GF['surface'][lead][i] = Ws.I

    def cal_self_energy(self):
        for i in range(len(self.omega_list)):
            for lead in ('l', 'r'):
                self.self_energy[lead][i] = \
                    self.D['lead_center'][lead]*self.GF['surface'][i][lead]*(self.D['lead_center'][lead].T)

    def get_D_matrix(self, i, j):
        if i == j:
            return self.D['on_site'][i]
        if i == j - 1:
            return self.D['couple'][i]
        if i == j + 1:
            return self.D['couple'][j].T
        else:
            return zeros((self.size['c'], self.size['c']))

    def get_M_matrix(self, i, j, omega):
        return (omega + 1j*self.delta)**2*eye(self.size['c']) - self.get_D_matrix[i,j]

    def cal_GF(self):
        for i in range(len(self.omega_list)):
            omega = self.omega_list[i]
            g = zeros(self.length).tolist()
            g[0] = (self.get_M_matrix(0, 0, omega) - self.self_energy['l'][i]).I
            for j in range(1, self.length - 1):
                g[j] = (self.get_M_matrix(j, j, omega) -
                        self.get_M_matrix(j, j-1, omega)*g[j-1]*self.get_M_matrix(j-1, j, omega)).I
            g[self.length - 1] = (self.get_M_matrix(j, j, omega) - self.self_energy['r'][i] -
                                  self.get_M_matrix(j, j-1, omega)*g[j-1]*self.get_M_matrix(j-1, j, omega)).I
            G = self.GF['center'][i]
            G[self.length - 1] = g[self.length - 1]
            for j in list(range(self.length - 1))[::-1]:
                G[j] = g[j](1 + self.get_M_matrix(j, j+1, omega)*G[j+1]*self.get_M_matrix(j+1, j, omega)*g[j])





