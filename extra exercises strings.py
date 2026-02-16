s = "Yo, banana boy!"
cleaned = s.lower().replace(" ", "").replace("!", "").replace(",", "")
print(cleaned)

if cleaned == cleaned[::-1]:
    print("The sentence 'Yo, banana boy!' is a palindrome")
else:
    print("The sentence 'Yo, banana boy!' is not a palindrome")



text = input("Enter text: ").lower()
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(count)