# Parametry modelu SIR dla różnych chorób

class Disease:
    def __init__(self, beta, gamma, name):
        self.beta = beta
        self.gamma = gamma
        self.name = name


# COVID-19
covid19 = Disease(beta=0.2, gamma=1. / 10, name='covid19')

# Grypa
flu = Disease(beta=0.3, gamma=1. / 3, name='flu')

# Odra
measles = Disease(beta=0.9, gamma=1. / 14, name='measles')
