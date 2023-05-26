# Parametry modelu SIR dla różnych chorób

class Disease:
    def __init__(self, beta, gamma):
        self.beta = beta
        self.gamma = gamma


# COVID-19
covid19 = Disease(beta=0.2, gamma=1. / 10)

# Grypa
flu = Disease(beta=0.3, gamma=1. / 3)

# Odra
measles = Disease(beta=0.9, gamma=1. / 14)
