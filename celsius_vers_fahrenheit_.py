def celcius_vers_fahrenheit(temperature_c):
    """
    La fonction fait la conversion de celsius à fahrenheit.
    argument température_c: la température en celsius
    retour : température en fahrenheit 
    """

    temperature_f = temperature_c * 9/5 + 32
    return temperature_f

print(celcius_vers_fahrenheit(temperature_c=0)) #devrait afficher 32.0
print(celcius_vers_fahrenheit(temperature_c=100)) #devrait afficher 212.0