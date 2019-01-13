magicians = ['alice','david','harry','dave']
#try to keep variables in understandable context
for magician in magicians:
    print(magician.title())

magicians = ['alice','david','harry','dave']
for magician in magicians:
    print(magician.title()+", That was a great trick!")
    #any indention is considered inside the loop
    print("I can't wait to see your new trick, " + (magician.title()+"\n"))
print("Thank you everyone! That was an amazing show!")