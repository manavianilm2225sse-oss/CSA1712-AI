
# Planets Database

planets = {
    "Mercury": 1,
    "Venus": 2,
    "Earth": 3,
    "Mars": 4,
    "Jupiter": 5,
    "Saturn": 6,
    "Uranus": 7,
    "Neptune": 8
}

print("PLANETS DATABASE")
for name, position in planets.items():
    print(name, "-", position)

print("\nInner Planets:")
for name, position in planets.items():
    if position <= 4:
        print(name)

print("\nOuter Planets:")
for name, position in planets.items():
    if position > 4:
        print(name)
