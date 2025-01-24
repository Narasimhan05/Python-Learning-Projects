#mail separation

email = input('Enter your email: ')

index = email.index('@')

username = email[:index]
domain = email[index + 1:]

print(f'Your username is {username}')
print(f'Your domain is {domain}')