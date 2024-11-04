class Temperature:
    def __init__(self, temperature, unit='C'):
        self.temperature = temperature
        self.unit = unit

    def convert_to_fahrenheit(self):
        if self.unit == 'C':
            return (self.temperature * 9/5) + 32
        return self.temperature

    def convert_to_celsius(self):
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9
        return self.temperature

class WindSpeed:
    def __init__(self, wind_speed, unit='kmh'):
        self.wind_speed = wind_speed
        self.unit = unit

    def convert_to_kmh(self):
        if self.unit == 'knots':
            return self.wind_speed * 1.852
        return self.wind_speed

    def convert_to_knots(self):
        if self.unit == 'kmh':
            print(self.wind_speed, "kmh")
            return self.wind_speed / 1.852
        return self.wind_speed

def WindChill(temperature, wind_speed, temp_unit='C', speed_unit='kmh'):
    temperature = Temperature(temperature, temp_unit)
    wind = WindSpeed(wind_speed, speed_unit)

    temp = temperature.convert_to_celsius()
    wind_speed = wind.convert_to_kmh()
    
    if wind_speed == 0:
        return None
    elif temp <= 0 and wind_speed >= 5:
        windchill = (13.12 + 0.6215 * temp - 11.37 * wind_speed**0.16 + 0.3965 * temp * wind_speed**0.16)
        return windchill
    elif temp <= 0 and 0 < wind_speed < 5:
        windchill = (temp + ((-1.59 + 0.1345 * temp) / 5) * wind_speed)
        return windchill
    else:
        return None
    
# Example usage
temperature = 10
wind_speed = 0.539957

print(WindChill(temperature, wind_speed, 'C', 'knots'))
print(WindChill(-10, 0.539957, 'C', 'knots'))
print(WindChill(14, 1, 'F', 'kmh'))
print(WindChill(-10, 6, 'C', 'kmh'))
print(WindChill(-10, 1, 'C', 'kmh'))





  