'''
Im working on learning git command line to collaborate
this is just a simple program so i can add to it, share it
    upload and download it and learn git without messing up a real program
'''
print('We can add two numbers!\n')
num1 = int(input("First number: "))
num2 = int(input("\nSecond number: "))
added = num1+num2
print("\n The result of %i + %i is %i." %(num1,num2,added))

yn = int(input('\n Do you want to add a third number? Press 1 for yes and 0 for no.'))

if yn ==1:
    num3 = int(input("\n Third Number: "))
    added2 = added+ num3
    print("\n The result of %i + %i + %i is %i" %(num1,num2,num3,added2))

print("\n Thanks for using! \n")

