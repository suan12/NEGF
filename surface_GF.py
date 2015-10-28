from environment import *

# constructing matrices
f = 1.0
omega = 1.5
delta = 0.00000000000000000000001
epsilon = 0.000000000001

D11 = matrix([2*f])
D22 = matrix([2*f])
D12 = matrix([-f])
I = matrix(eye(1))

# calculate surface GF

Ws = ((omega + 1j*delta)**2)*I - D11
Wb = ((omega + 1j*delta)**2)*I - D22
tau1 = D12
tau2 = tau1.T

while abs(tau1).max() > epsilon:
    Wb_I = Wb.I
    Ws = Ws - tau1*Wb_I*tau2
    Wb = Wb - tau1*Wb_I*tau2 - tau2*Wb_I*tau1
    tau1 = tau1*Wb_I*tau1
    tau2 = tau2*Wb_I*tau2
print(Ws.I)