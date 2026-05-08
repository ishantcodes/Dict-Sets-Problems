#Write a program to create a dictionary of Hindi words with values as their English
#translation. Provide user with an option to look it up!
dicto = {
    "baccha": "kid",
    "billi": "cat",
    "kutta": "dog",
    "bhess": "buffalo"
}

word = input("Give a word you want meaning of: ")
print(dicto.get(word))
