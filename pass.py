import random

wordlist=[]
with open("lfc.txt", 'r') as file:
    data=file.readlines()
    for line in data:
        words=line.split()
        for item in words:
            if len(item)>=5:
                wordlist.append(item.capitalize())
schar=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ',', ';', ':', '<', '>', '/', '.', '\\', ']', '|', '[', '{', '}', '?', '`', '~']
word = random.choice(wordlist)
special = random.choice(schar)
num= random.randint(10, 99)
password= word+special+str(num)
print(password)
