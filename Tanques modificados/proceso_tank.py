import numpy as np
import matplotlib.pyplot as plt
import math
import random
import scipy.io

# --------parametros deñ sistema---------
# Parameters value of three?tank system
mu13 = 0.5 * 10
mu20 = 0.675 * 10
mu32 = 0.5 * 10

S = 0.0154
Sn = 50 * 5e-5
W = math.sqrt(2 * 9.81)

# Output operat ing Points (m)
Y10 = 0.400
Y20 = 0.200
Y30 = 0.300

# Input operat ing Points (m3/s )
U10 = 0.350e-004
U20 = 0.375e-004

# Matrix A
A11 = 0.994347447187946  # -(mu13 * Sn * W) / (2 * S * math.sqrt(Y10 - Y30))
A12 = 0.000016

A13 = 0.0056  # -A11

A21 = A12  # 0
A23 = 0.0056  # (mu32 * Sn * W) / (2 * S * math.sqrt(Y30 - Y20))

A22 = 0.989  # -A23 - ((mu20 * Sn * W) / (2 * S * math.sqrt(Y20)))

A31 = A23  # -A11
A32 = A23
A33 = 0.9887  # -A32 - A31

# Matrix B
B11 = 0.0648  # 1 / S
B12 = 0

B21 = 0
B22 = 0.0646  # 1 / S

B31 = 0.0002
B32 = 0.0002

Ad = np.array([[A11, A12, A13],
               [A21, A22, A23],
               [A31, A32, A33]])
# print(Ad[0,0])
Bd = np.array([[B11, B12],
               [B21, B22],
               [B31, B32]])

# --------parametros deñ sistema---------
tm = 0.001
n = 60 * 200
t = tm*np.linspace(0, n, num=n)

# ----------variables--------
# ----------referencias--------
q1 = []
q2 = []
# ----------referencias--------
# ----------estados--------
x1 = []
x2 = []
x3 = []
# ----------estados--------

# ----------controlador--------
u1c = []
u2c = []
ek1 = 0
ek2 = 0
uk1 = 0
uk2 = 0
# ----------controlador--------


# -----------inicializacion----------
u1c = np.append(u1c, 0)
u2c = np.append(u2c, 0)
x1 = np.append(x1, 0)
x2 = np.append(x2, 0)
x3 = np.append(x3, 0)
ref1 = random.uniform(0.3532, 0.4471)
ref2 = random.uniform(0.1858, 0.2474)
t1 = int(random.uniform(350, 750))
t2 = int(random.uniform(350, 750))
q1 = np.append(q1, ref1)
q2 = np.append(q2, ref2)

for i in range(len(t) - 1):
    e1 = q1[i] - x1[i]
    e2 = q2[i] - x2[i]

    # calculo la accion de control u1 y u2

    u1 = 0.65 * e1 - 0.61 * ek1 + uk1
    u2 = 0.65 * e2 - 0.61 * ek2 + uk2
    ek1 = e1
    ek2 = e2
    uk1 = u1
    uk2 = u2

    # calculo    los    estados
    x = np.array([[x1[i]], [x2[i]], [x3[i]]])
    # print('x1 ,', x[1])
    u = np.array([[u1], [u2]])

    x_k1 = np.matmul(Ad, x) + np.matmul(Bd, u)

    # ----------actualizacion----------
    # print(i)
    u1c = np.append(u1c, u1)
    u2c = np.append(u2c, u2)
    x1 = np.append(x1, x_k1[0])
    x2 = np.append(x2, x_k1[1])
    x3 = np.append(x3, x_k1[2])
    # -------cambios de referencia---------

    # -------cambios de referencia---------
    if i == t1:
        t1 = int(random.uniform(t1 + 350, t1 + 350 + 750))
        ref1 = random.uniform(0.3532, 0.4471)
    if i == t2:
        t2 = int(random.uniform(t2 + 350, t2 + 350 + 750))
        ref2 = random.uniform(0.1858, 0.2474)
    q1 = np.append(q1, ref1)
    q2 = np.append(q2, ref2)
    # ----------actualizacion----------
    # print(i)
# print(x1.shape)
x1 = x1.reshape(x1.shape[0], 1)
x2 = x2.reshape(x2.shape[0], 1)
x3 = x3.reshape(x3.shape[0], 1)
u1c = u1c.reshape(u1c.shape[0], 1)
u2c = u2c.reshape(u2c.shape[0], 1)
q1 = q1.reshape(q1.shape[0], 1)
q2 = q2.reshape(q2.shape[0], 1)

if False:
    scipy.io.savemat('datos_attack_2.mat',
               {'x1': x1, 'x2': x2, 'x3': x3, 'u1': u1c, 'u2': u2c, 'q1': q1, 'q2': q2, 'al1': al1, 'al2': al2,
               'al3': al3, 'al4': al4})

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, x1, 'b', linewidth=1.2)
plt.plot(t, q1, '--r', linewidth=1)
plt.legend(['$x_1$', '$q_1$'], loc='lower right')
plt.ylabel('Nivel 1 (m)')
plt.grid()
#plt.xlim(0, 2000)
# plt.xlim(2000,4000)
# plt.ylim(0.32, 0.58)
plt.subplot(3, 1, 2)
plt.plot(t, x2, 'b', linewidth=1.2)
plt.plot(t, q2, '--r', linewidth=1)
plt.legend(['$x_2$','$q_2$'], loc='lower right')
plt.ylabel('Nivel 2 (m)')
#plt.xlim(0, 2000)
# plt.xlim(2000,4000)
# plt.ylim(0.15, 0.4)
plt.grid()
plt.subplot(3, 1, 3)
plt.plot(t, x3, 'b', linewidth=1.2)
plt.xlabel('Tiempo(s)')
plt.ylabel('Nivel 3 (m)')
#plt.xlim(0, 2000)
plt.legend(['$x_3$'], loc='lower right')
plt.grid()

plt.show()

