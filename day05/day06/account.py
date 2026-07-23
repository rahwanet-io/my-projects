word = "sas"
reverse = ""

for char in word:
    reverse = char + reverse

if word == reverse:
    print("The reverse is also", reverse)
else:
    print("The reverse is not the same")