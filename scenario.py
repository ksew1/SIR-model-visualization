class Scenario:
    def __init__(self, S0, I0, R0):
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0

# Początek epidemii w całkowicie podatnej populacji
start_in_susceptible_pop = Scenario(S0=1.0, I0=0.0, R0=0.0)

# Epidemia w populacji, gdzie już wystąpiły infekcje
epidemic_in_infected_pop = Scenario(S0=0.95, I0=0.05, R0=0.0)

# Epidemia w populacji, gdzie niektóre osoby już wyzdrowiały
epidemic_in_recovered_pop = Scenario(S0=0.8, I0=0.1, R0=0.1)

# Początek epidemii w populacji, która jest częściowo odporna na chorobę
start_in_partially_immune_pop = Scenario(S0=0.8, I0=0.0, R0=0.2)