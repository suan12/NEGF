import numpy as np

f = 1.0
omega = 3.999
delta = 0.000000000000000000001
epsilon = 0.0000001

D11 = np.matrix([f])
D22 = np.matrix([2*f])
D12 = np.matrix([-f])
I = np.matrix([1.0])

Ws = (omega + 1j*delta)*I - D11
Wb = (omega + 1j*delta)*I - D22
tau1 = D12

while max(abs(tau1)) > epsilon:
    tau2 = tau1.T
    Wb_I = Wb.I
    Ws = Ws - tau1*Wb_I*tau2
    Wb = Wb - tau1*Wb_I*tau2 - tau2*Wb_I*tau1
    tau1 = tau1*Wb_I*tau1

print(Ws.I)