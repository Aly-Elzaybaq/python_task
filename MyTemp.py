#1.fahrenheit_to_celsius : its equation (Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32)

def fahrenheit_to_celsius():
    Fahrenheit = float(input("input the degrees in Fahrenheit (°F) " ))
    Celsius  = float(Fahrenheit * 9/5) + 32
    return Celsius
Celsis_result = fahrenheit_to_celsius()
print ( "Temperature in udegrees Celsis (°C) =" + str(Celsis_result))

#2.celsius_to_fahrenheit: its equation (Temperature in udegrees Celsis (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9)
def celsius_to_fahrenheit():
    Celsius =  float(input("input the degrees in Celsius (°C) " ))
    Fahrenheit  = float(Celsius - 32) * 5/9
    return Fahrenheit
Fahrenheit_result = celsius_to_fahrenheit()
print ( "Temperature in degrees Fahrenheit (°F) = " + str(Fahrenheit_result))
