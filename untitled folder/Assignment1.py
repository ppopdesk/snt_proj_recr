import hashlib
from datetime import datetime

input_string = input("Enter a string ")

target = int("0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",16)
main_hexa = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
i = 0
copy_of_input_string = input_string + str(i)
start_time = datetime.now()

while int(hashlib.sha256(copy_of_input_string.encode('utf-8')).hexdigest(),16)>=target:
    i+=1
    copy_of_input_string = input_string + str(i)

end_time = datetime.now()

print(f"Number to be appended to input string : {i}")
print(f"Hash of resulting string : {hashlib.sha256(copy_of_input_string.encode('utf-8')).hexdigest()}")
print(f"Time taken for program to run : {end_time-start_time}")