## WeC_Systems_Cryptography

My solution approach to solving the WeC Crytography challenge

<br>

# **Step 1** 

Scan the QR Code

> R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ==

Scanning the QR Code in the document gives us the above encrypted text. Upon obervation this string can be seen to have characters ranging from [a-b], [A-B], [0-9] and even '='.
A similar character set can be observed in *Base64* syntax.

<br>

# **Step 2**

Run the string through a [*Base64*](#base64) *decrypter*

> Great job. Julius Caeser was born in the 100 BC:
PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F
OPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY

The oddly specific mention of the king 'Julius Caesar' indicates that the initial message has been passed through a *Caesar cipher*. Hence, in-order to reverse it, we will now be applying *Caesar Cipher* on the encrypted message.

<br>

# **Step 3**

Decrypt the message using a *Caesar Cipher* (upon observation we get that a shift = +22 will output a readable message)

> THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J
STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC

The message 'cipher keysquare without J' is a clear implication of the necessary usage of the *Playfair cipher* in which a 5x5 keysquare is usually made to decrypt the message while excluding the 'J' alphabet (usually)

<br>

# **Step 4**

Decrypt the message using a *Playfair cipher* with a keysquare *'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*

> RSAENCRYPTNUMBERTWOHUNDREDFOURTYTHREEWITHNVALUEASTWOTHOUSANDFOURHUNDREDANDNINETEENANDEVALUEASELEVENX

Expanding this string into a more readable format return `RSA ENCRYPT NUMBER TWO HUNDRED FOURTY THREE WITH N-VALUE AS TWO THOUSAND FOUR HUNDRED AND NINETEEN AND E-VALUE AS ELEVEN X.` 

<br>

# **Step 5**

As per the above result, run the `243` through an RSA encrypter with `n = 2419` and `e = 11`

> Encrypted message = 1982

The encrypted message we get after running the rsa algorithm returns the password for the zip file. Opening the `.txt` file further returns a string

> TM, DTZ KTZSI RJ😔. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?🤨

<br>

# **Step 6**

Run the above string through a caesarcipher (+5) decoder.
> OH, YOU FOUND ME😔. CONGRATS. THIS IS THE ENDGOAL. OR IS IT?🤨


<br><br>

<a name = 'base64'>Base64</a>