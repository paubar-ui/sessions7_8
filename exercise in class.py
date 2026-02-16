s = "Red Roses run no risk, sir, on nurses order."
punctuation = " ,."
for p in punctuation:
    s = s.replace(p,"")
print(s)

s = s.upper()
if s == s[::-1]:
    print("f{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")