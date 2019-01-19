banned_user = ['andrew','kim','john','sarah']
user = 'kelly'
if user not in banned_user:
    print(user.title()+ ", you have been logged in successfully!")


banned_user = ['andrew','kim','john','sarah']
user = 'john'
if user in banned_user:
    print(user.title()+ ", sorry due to being an asshat you are banned from www.example.com")