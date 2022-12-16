from linereader import read_lines as get

data = get('6.input.txt', ')')


def path_to_com(planet, n=0, target='COM'):
    if planet == target:
        return n

    return path_to_com(orbits[planet], n + 1, target)


orbits = {}

for orbit_system in data:
    orbits[orbit_system[1]] = orbit_system[0]

# Part2
me = 'YOU'
santa = 'SAN'

santa_len = path_to_com(santa)
my_len = path_to_com(me)

x = -2

for i in range(0, max(santa_len, my_len)):
    if me == santa:
        break

    if santa_len > my_len:
        santa = orbits[santa]
        santa_len -= 1
        x += 1
    elif my_len > santa_len:
        me = orbits[me]
        my_len -= 1
        x += 1
    else:
        me = orbits[me]
        santa = orbits[santa]
        x += 2

print("Bla bla stuff output: ", x)
