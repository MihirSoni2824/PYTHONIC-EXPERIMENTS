import re

text = "The quick brown fox jumps over the lazy dog."

# Match the word "fox"
match = re.search("fox", text)
if match:
    print("Found 'fox' at index:", match.start())

# Find all digits
digits = re.findall("[0-9]+", "12345 abc 678")
print(digits)  # Output: ['12345', '678']

# Replace all vowels with 'X'
new_text = re.sub("[aeiou]", "X", text)
print(new_text)  # Output: "THX qXick brXwn fX jumps XVXr thx lazy dXg."