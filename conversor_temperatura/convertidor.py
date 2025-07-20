def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

# Testeo básico
if __name__ == "__main__":
    temp = 10
    print(f"{temp}°C -> {celsius_to_fahrenheit(temp)}°F")
    print(f"{temp}°C -> {celsius_to_kelvin(temp)}K")
