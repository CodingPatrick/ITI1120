def print_vowels(phrase):
    '''
    (str) -> None

    Prints all the vowels in the phrase.
    '''
    for character in phrase:
        if character.lower() not in "aeiou":
            print(character)
    
phrase = input("Give me a phrase:")
print("The vowels are:")
print_vowels(phrase)
