# variable
a = 1 
b = 'String'
c = True
print(a, b, c)

# f string is concat staring
print(f'c is {c}, {a}')

# list
l = [1, 3, 4]
print(l)

# tuple is immutable
t = (1, 3, 4, 5)
print(t)


# dict 

dt  = {
    'name': 'keng',
    'team': 'ODDS',
}
print(dt)
print(dt['name'])
print(dt.keys())
print(dt.values())
print(dt.items())

# challent
print(f'l at index 0: {l[0]}')
print(f't at index 1: {t[0]}')
print(f'dt at key team: {dt["team"]}')

# condtion 
a = 3
if a == 1: 
    print('a')
elif a == 2: 
    print('equle 2')
else: 
    print('not equle')

l = [1, 3, 4, 5]

for item in l:
    print(item)
    if item == a:
        print('yeah')