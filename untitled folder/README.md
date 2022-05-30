After importing the required libraries, we ask for string input from user.
We then initialise the target variable which is a integer (converted from hexadecimal string to base 10 integer)
main_hexa variable is the sha256 output of the input string and copy variable is the copy of the input string. 
We append numbers starting from 0 to the copy string and convert it to hex and check whether it is less than target variable. If yes, that is the number we are looking for.

Input example:
"IITK"
Output:
Number to be appended to input string : 438251
Hash of resulting string : 00000ea354286b4e6f46212409f5c32a44c6e741b5d66984632be36a4abafc9c
Time taken for program to run : 0:00:00.500172
