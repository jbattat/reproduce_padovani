import numpy as np

# "Padovani" model for proton and electrons
def crSpectrum(E, species='pH'):
    # alpha=-0.8, beta=1.9, C=2.4e15, E0=650e6):
    if species == 'pH':  # proton, "high"
        C, E0, alpha, beta = 2.4e15, 650e6, -0.8, 1.9
    elif species == 'pL': # proton, "low"
        C, E0, alpha, beta = 2.4e15, 650e6, 0.1, 2.8
    elif species == 'elec': # electron
        C, E0, alpha, beta = 2.1e18, 710e6, -1.3, 1.9
    else:
        print(f"Unrecognized species: {species}")
        return E
    return C*E**alpha/(E+E0)**beta


# Compute the range of a particle (proton) given an energy loss function
# by integrating the energy loss function until the particle is at rest.
def rangeOfE(EE, dEdN):
    # Einit: initial particle energy [eV]
    # dEdN: energy loss function (1e-16 eV cm2)
    # EE: corresponding energies for dEdN (eV)
    dE = EE[1:]-EE[:-1]

    ranges = []
    #nn = len(dEdN)-1
    nn = len(dE)
    
    integrand = dE/dEdN[1:]
    for ii in range(nn):
        ranges.append(np.sum(integrand[0:ii]))

    return ranges


# Helper functions to go between column and surface density (N and Sigma)
def N_of_Sigma(sigma, Abar=2): 
    # compute the column density for a given surface density
    # sigma given in g/cm2, N given in 1/cm2
    # Abar is the mean molecular weight of the medium (Abar=2 for molecular hydrogen H2)
    mp = 1.67262192e-24 # gram
    return sigma/(Abar*mp)

def Sigma_of_N(NN, Abar=2): 
    # compute the column density for a given surface density
    # sigma given in g/cm2, N given in 1/cm2
    # Abar is the mean molecular weight of the medium (Abar=2 for molecular hydrogen H2)
    mp = 1.67262192e-24 # gram
    return Abar*mp*NN
