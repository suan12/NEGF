from environment import *
from scipy.sparse import csc_matrix
from scipy.sparse import eye as sparse_eye
from scipy.sparse.linalg import inv as sparse_inv


class Lead(object):

    def __init__(self, D00, D01, D11):
        self.D00 = csc_matrix(D00)
        self.D01 = csc_matrix(D01)
        self.D11 = csc_matrix(D11)
        self.size = D00.shape[0]
        self.gf = None

    def cal_surface_gf(self, E, order=2, delta=0.000001, epsilon=0.000001):
        I = sparse_eye(self.size).tocsc()
        if order == 1:
            ws = (E + 1j*delta)*I - self.D00
            wb = (E + 1j*delta)*I - self.D11
        else:
            ws = ((E + 1j*delta)**2)*I - self.D00
            wb = ((E + 1j*delta)**2)*I - self.D11
        tau1 = self.D01
        tau2 = tau1.H
        while abs(tau1).max() > epsilon:
            wb_I = sparse_inv(wb)
            ws = ws - tau1*wb_I*tau2
            wb = wb - tau1*wb_I*tau2 - tau2*wb_I*tau1
            tau1 = tau1*wb_I*tau1
            tau2 = tau2*wb_I*tau2
        self.gf= sparse_inv(ws)


class Coupling(object):

    def __init__(self, lead, position, D_couple):
        self.lead = lead
        self.position = position
        self.D_couple = csc_matrix(D_couple)
        self.self_energy = None

    def cal_self_engergy(self, E, order=2, delta=0.000001, epsilon=0.000001):
        lead = self.lead
        lead.cal_surface_gf(E, order, delta, epsilon)
        D_couple = self.D_couple
        self.self_energy = D_couple*lead.gf*D_couple.H


class System(object):

    def __init__(self, D, couplings, E, order=2, delta=0.000001, epsilon=0.000001):
        """
        :param D: should be something like {'on_site': [D00, D11, ...], 'couple': [D01, D12, ...]}
        :param leads: should be something like [coupling, ..]
        """
        # store values
        self.D = {'on_site': [], 'couple': []}
        for D_on_site in D['on_site']:
            self.D['on_site'].append(csc_matrix(D_on_site))
        for D_couple in D['on_site']:
            self.D['couple'].append(csc_matrix(D_on_site))
        self.E = E
        self.couplings = couplings
        self.delta = delta
        self.epsilon = epsilon
        self.order = order

        # initializing
        self.length = len(D['on_site'])
        self.size = [D['on_site'][i].shape[0] for i in range(self.length)]
        self.self_energy = [0]*self.length
        self.gf = [[None]*self.length for i in range(self.length)]
        self.T = matrix(zeros((len(couplings), len(couplings))))
        self.g = [0]*self.length

        for coupling in couplings:
            coupling.cal_self_engergy(E, order, delta, epsilon)
            self.self_energy[coupling.position] += coupling.self_energy


    def M(self, i, j):
        """
        return M matrices according to indices
        """
        if i == j:
            size = self.size[i]
            if self.order == 1:
                return (self.E + 1j*self.delta)*sparse_eye(size).tocsc() - self.D['on_site'][i] - self.self_energy[i]
            else:
                return (self.E + 1j*self.delta)**2*sparse_eye(size).tocsc() - self.D['on_site'][i] - self.self_energy[i]
        if i + 1 == j:
            return -self.D['couple'][i]
        if i == j + 1:
            return -self.D['couple'][j].H
    '''
    def get_index(self, i):
        return sum(self.size[0:i])

    def gen_sparse_M(self):
        from scipy import sparse
        sparse_M = sparse.lil_matrix((self.total_length, self.total_length))
        for i in range(self.length):
            sparse_M[sum(self.size[0:i]):sum(self.size[0:i + 1]), sum(self.size[0:i]):sum(self.size[0:i + 1])] = \
            self.M(i, i)
            if i != self.length - 1:
                sparse_M[sum(self.size[0:i]):sum(self.size[0:i + 1]), sum(self.size[0:i + 1]):sum(self.size[0:i + 2])] \
                = self.M(i, i + 1)
                sparse_M[sum(self.size[0:i+1]):sum(self.size[0:i + 2]), sum(self.size[0:i]):sum(self.size[0:i + 1])] \
                = self.M(i + 1, i)
        self.sparse_M = sparse_M.tocsc()


    def cal_sparse_gf(self):
        from scipy.linalg import inv
        self.sparse_gf = inv(self.sparse_M)
    '''

    def cal_diag_gf(self):
        """
        calculate diagonal green's function for center area.
        """
        length = self.length
        g = self.g
        # forward iterating
        g[0] = sparse_inv(self.M(0, 0))
        for j in range(1, length):
            g[j] = sparse_inv(self.M(j, j) -
                    self.M(j, j-1)*g[j-1]*self.M(j-1, j))

        G = self.gf
        G[self.length - 1][self.length - 1] = g[self.length - 1]
        # calculate more green's function according to the flag
        # backward iterating
        for j in list(range(self.length - 1))[::-1]:
            G[j][j] = g[j] + g[j]*self.M(j, j+1)*G[j+1][j+1]*self.M(j+1, j)*g[j]


    def cal_gf(self, i, j):
        """
        calculate G_ij for center area
        """
        from operator import mul
        G = self.gf
        if i == j or G[i][j] is not None:
            return None
        if i > j:
            i, j = j, i
        g = self.g
        G[i][j] = reduce(mul, [g[k]*-self.M(k, k+1) for k in range(i, j)], 1)*G[j][j]
        G[j][i] = G[i][j]


    def cal_T(self, i, j):
        """
        calculating transmission probability from lead i to lead j
        """
        ic= self.couplings[i].position
        jc= self.couplings[j].position
        self.cal_gf(ic, jc)
        gamma_i = 1j*(self.couplings[i].self_energy - self.couplings[i].self_energy.H)
        gamma_j = 1j*(self.couplings[j].self_energy - self.couplings[j].self_energy.H)
        self.T[i, j] = trace((gamma_j*self.gf[ic][jc].H*gamma_i*self.gf[ic][jc]).todense()).real
        self.T[j, i] = self.T[i, j]
