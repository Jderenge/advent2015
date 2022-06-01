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
    hash = hash.hexdigest(ninput)
    # # Check new hashcheck to see if hash starts with 5 leading zeros
    newhash = hash.hexdigest(ninput)
    if newhash([0,6] == checker):
        print(counter)
        quit
    # # If it does, print counter and break
    counter +=  1   #yo