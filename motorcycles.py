#motorcycles

motorcycles = ['honda','harley','suzuki','indian','yamaha']
motorcycles.append('ducati')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('harley')
motorcycles2.append('suzuki')
motorcycles2.append('indian')
motorcycles2.append('yamaha')

print(motorcycles2)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[0]
del motorcycles[-1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda','harley','suzuki','indian','yamaha']
last_whip = motorcycles.pop(0)
print("The Last motorcycle I rode on was a " + last_whip.title()+ "!")

motorcycles=['honda','suzuki','ducati','zoomie']
motorcycles.remove('ducati')
print(motorcycles)


motorcycles=['honda','suzuki','ducati','zoomie']
print(motorcycles)
too_expensive='zoomie'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA" + too_expensive.title()+ " is too expensive for me.")