class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def convert_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32
    
    def convert_to_celsius(self):
        return (self.temperature - 32) * 5/9
    
class WindSpeed:
    def __init__(self, wind_speed):
        self.wind_speed = wind_speed

    def convert_to_kmh(self):
        return self.wind_speed * 1.60934
    
    def convert_to_knots(self):
        return self.wind_speed / 1.852
    

def WindChill(temperature, wind_speed):
    temperature = Temperature(temperature)
    wind_speed = WindSpeed(wind_speed)

    temp = temperature.temperature
    wind_speed = wind_speed.wind_speed

    if temp <= 0 and wind_speed >= 5:
        windchill = 13.12 + 0.6215 * temp - 11.37 * wind_speed**0.16 + 0.3965 * temp * wind_speed**0.16
        return windchill
    else: 
        windchill = temp + ((-1.59 + 0.1345 * temp) / 5) * wind_speed
        return windchill

temperature = -10
wind_speed = 1

print(WindChill(temperature, wind_speed))





