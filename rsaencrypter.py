n = int(input('Enter the n-value (public key): '))
e = int(input('Enter the e-value: '))

m = int(input('\nEnter the value to be encrypted: '))

print(f'\nEncrypted message: {m**e % n}')