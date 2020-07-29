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