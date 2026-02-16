print("heLLO WORLd".capitalize())

print("BOB".center(22, '*'))

# "find" finds the position qhere a substring can be found

s = "I see a cat on the street. the street is nice. the cat is black"
print("the position of cat is:", s.find('cat'))
print("the position of the next cat is:", s.find("cat", 9))
print("find returns -1 if we can not find it:", s.find("dog"))
emails = "bob@gmail, and also alice@yahoo, and even bea@icloud.com"

#how many emails? - count method only counts inside the string
print(emails.count("@"))
pos = 0
while True:
    pos = emails.find("@", pos)
    if pos == -1:
        break
    print("Found one email at position", pos)
    pos += 1

#replace will replace part of a string with another one
print(s)
print(s.replace("cat", "parrot"))
print(s.replace(" ", "|"))

#split will break the string into components based on the key
print(s.split())
