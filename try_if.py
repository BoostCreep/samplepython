color = 'blue'
print("Is the color == 'blue' ? I predict True.")
print(color == 'blue')

color = 'green'
print("\nIs the color == 'blue'? I predict false!")
print(color == 'blue')

color = 'silver'
print("\nIs the color == 'blue'? Not a chance!")
print(color == 'blue')

number = 31
color = 'green'
if number !=31 and color == 'green':
    print("\nSorry, this is not the right number and color!")
if number ==31 and color == 'green':
    print("\nYou have guessed the correct number and color!")

colors = ['green','blue','silver','purple','white','black','gold']
print(colors)
color = 'yellow'
if color != colors:
    print("\nWARNING! This color is not included in the presets!")