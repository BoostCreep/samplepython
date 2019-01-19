#4-3 Count to Twenty
numbers = []
for value in range (1,21):
    numbers.append(value)
print(numbers)



#Using min/max 
numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))
#counting odd
odd = list(range (1,20,2))
print(odd)
#counting by 3
threes = list(range(3,31,3))
for number in threes:
    print(number)
#Cubes
cubes = []
for number in range(1,11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#interation on Cube
cubes = [number**3 for number in range (1,11)]

for cube in cubes:
    print(cube)

