# Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)

class Weather:

    def __init__(self, temperature, humidity, wind_speed):
        self.weather_parameters = {
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
        }

    def __contains__(self, item):
        return item in self.weather_parameters.values()

    def __str__(self):
        return f"Weather Parameters: {self.weather_parameters}"


# Example usage
weather = Weather(temperature=30, humidity=70, wind_speed=15)
print(weather)
print("Is 30 in weather parameters?", 30 in weather)  # True
print("Is 25 in weather parameters?", 25 in weather)  # False
