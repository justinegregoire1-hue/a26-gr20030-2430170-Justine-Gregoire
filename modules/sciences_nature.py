def energie_cinetique(masse, vitesse):
    """
    La fonction calcule l'énergie cinétique 
    e = 1/2(masse * vitesse**2)
    masse : en kg
    vitesse : en m/s
    retourne : énergie cinétique J
    """

    e = masse * vitesse ** 2 * 0.5
    return e