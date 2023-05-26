import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from disease import covid19 as disease
from scenario import epidemic_in_infected_pop as scenario

# Parametry modelu
beta = disease.beta
gamma = disease.gamma


# Definicja modelu SIR
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]


# Początkowe warunki
S0 = scenario.S0
I0 = scenario.I0
R0 = scenario.R0
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
plt.title("SIR model of " + disease.name)
plt.show()
