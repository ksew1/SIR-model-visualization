import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from disease import covid19

# Parametry modelu
beta = covid19.beta
gamma = covid19.gamma


# Definicja modelu SIR
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]


# Początkowe warunki
S0 = 0.9
I0 = 0.1
R0 = 0.0
y0 = [S0, I0, R0]

# Czas
t = np.linspace(0, 100, 1000)

# Rozwiązanie równań różniczkowych
solution = odeint(sir_model, y0, t, args=(beta, gamma))
solution = np.array(solution)

# Wykres
plt.figure(figsize=[6, 4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("SIR model")
plt.show()
