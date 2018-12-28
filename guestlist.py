family_friends = ['russel','kim','barbra','Lex']
family_friends1 = family_friends.pop(1)
print("\nThe guest " + family_friends1.title() + " can not make it to the event.")
family_friends.insert(1,"bobby")
print("")
print(family_friends)

family_friends = family_friends.pop(0)
message = ("Congrat! " + (family_friends.title()) + " you have been invited to the party!")
print(message)
print(family_friends)