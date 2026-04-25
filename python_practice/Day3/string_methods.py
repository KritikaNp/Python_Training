# Using string methods:

# Remove extra spaces
# Make it title case
# Replace "python" with "coding"
# Split it into a list of words
sentence = "  my name is aarav and i love python  "
sentence = sentence.replace("python","coding")
sentence = sentence.strip()
sentence = sentence.title()
print(sentence)
words=sentence.split()
print(words)


# Take user's full name and print it in uppercase
full_name="Kritika Neupane"
print(full_name.upper())


# Count how many vowels are in a string
stri="hello"
count=0
for letter in stri:
    if letter in 'aeiou':
        count+=1
    
print(f"The number of vowels in {stri} is {count}")

# Reverse a string without using any built in reverse function
result=""
for i in range(len(stri)-1,-1,-1):
    result+=stri[i]
print(result)


#  Check if a string is a palindrome (reads same forwards and backwards) example: "racecar"
word="racecar"
reverse_word=""
for i in range(len(word)-1,-1,-1):
    reverse_word+=word[i]

if reverse_word==word:
    print("The given string is palindrome")
else:
    print("The giben string is not palindrome")


# Take a sentence and print each word on a new line
sentencee="Hi! My name is Kritika"
sentencee=sentencee.split()
for word in sentencee:
    print(word)