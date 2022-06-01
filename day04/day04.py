# Jonny Derenge

import hashlib

input = "bgvyzdsv"
counter = 0
checker = "00000"
while(1):
    ninput = input
    # Append number to end of input
    ninput += str(counter)
    # Hash new input
    newhash = hashlib.md5(ninput.encode())
    # # Check new hashcheck to see if hash starts with 5 leading zeros
    if (newhash.hexdigest()[0:5] == checker):
        print(counter)
        quit
    # # If it does, print counter and break
    counter += 1