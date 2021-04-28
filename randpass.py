import random

schar=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ',', ';', ':', '<', '>', '/', '.', '\\', ']', '|', '[', '{', '}', '?', '`', '~']
ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper=[]
for i in ch:
    upper.append(i.capitalize())
password=random.choice(upper)+random.choice(upper)+random.choice(ch)+random.choice(ch)+random.choice(schar)+str(random.randint(10,99))+random.choice(schar)
print(password)
