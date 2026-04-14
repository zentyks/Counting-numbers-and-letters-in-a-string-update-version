def count_letters_digits(text):
    letters = 0
    digits = 0
    for char in text:
        if char.isalpha():
            letters += 1
