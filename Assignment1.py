import hashlib
from datetime import datetime

string = input("Enter a string ")

target = int("0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",16)
main_hexa = hashlib.sha256(str.encode('utf-8')).hexdigest()
i = 0
copy = string + str(i)
start = datetime.now()

while int(hashlib.sha256(copy.encode('utf-8')).hexdigest(),16)>=target:
    i+=1
    copy = string + str(i)

end = datetime.now()

print(f"Number to be appended to string : {i}")

print(f"Time taken for program to run : {end-start}")

print(f"Hash of resulting string : {hashlib.sha256(copy.encode('utf-8')).hexdigest()}")