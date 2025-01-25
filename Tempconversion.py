def celsiustoFarenheit(celsius):
    Farenheit=(9/5*celsius) +32
    return f"Temperature from celsius to farenheit {Farenheit}"

def farenheittoCelsius(farenheit):
    Celsius=(5/9*farenheit)-32
    return f"Temperature from farenheit to celsius {Celsius}"

def celsiustoKelvin(celsius):
    Kelvin=celsius+273
    return f"Temperature from celsius to Kelvin{Kelvin}"

def farenheittoKelvin(farenheit):
    Kelvin=(farenheit-32)*5/9 + 273
    return f"Temperature from farenheit to Kelvin{Kelvin}"
    


print(celsiustoFarenheit(100))
print(farenheittoCelsius(22))
print(celsiustoKelvin(202))
print(farenheittoKelvin(33))

