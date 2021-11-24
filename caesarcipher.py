def caesarcipher(arr, shift):
    print(f'\n\nCaesar cipher (+{shift})')

    for i in arr:
        if i.isalpha():
            if ord(i) + shift > 90:
                print(chr(ord(i) + shift - 26), end='')
            else:
                print(chr(ord(i) + shift), end='')
        else:
            print(i, end='')

arr = input('Encoded string: ')

for i in range(1, 26):
    caesarcipher(arr.upper(), i)