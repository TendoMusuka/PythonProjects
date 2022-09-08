# Author : Rutendo Musuka
# Purpose :Bringing the old times back - Calculates your potential love partner using your names
# Source: https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love
# If buzzfeed says it works, who am I to question it
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_name = name1.lower() + name2.lower()
true = "true"
love = "love"
total_matches_in_true = total_matches_in_love = 0
for letter in true:
    match = combined_name.count(letter)
    total_matches_in_true += match

for letter in love:
    match = combined_name.count(letter)
    total_matches_in_love += match

love_score = total_matches_in_true * 10 + total_matches_in_love

print(f"Your love is {love_score}%")
