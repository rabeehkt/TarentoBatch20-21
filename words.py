"""
Question:

- Accept a String input
- Print the count of words in the String. Space is assumed to be the separator between words
- Print all numbers that are present in the String and also if they are odd or even. Numbers which are together should be counted as one number.

Eg. If the String input is
The boy had 2 apples, 23 oranges and 222 grapes.
then the output should be as below
Total words - 10
Even numbers - 2,222
Odd numbers - 23 

"""


string = input("Enter a string: ")
count=len(string.split());
print("Total words:",count)

even=[]
odd=[]

for word in string.split():
    if word.isdigit():
        if((int(word))%2==0):
             even.append(int(word))
        else:
             odd.append(int(word))
print("even numbers:",even)
print("odd numbers:",odd)
