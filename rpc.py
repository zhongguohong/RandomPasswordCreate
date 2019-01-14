import random
l1 = list(range(49,49+76)) #Use Ascii 49-76 code,mean 1-9 and A-Z and a-z and some symbols.
l2 = [chr(x) for x in l1] #Translate Ascii values into characters
l3 = [random.choice(l2) for x in range(32)] #Randomly select 32 passwords from the specified character set
s1 = ''.join(l3)  #Connect the character set as a string
print(s1)
