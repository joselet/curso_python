def c_to_f(c):
    return c * 9/5 + 32

c = float(input("Celsius: "))
print(f"{c}°C = {c_to_f(c)}°F")
