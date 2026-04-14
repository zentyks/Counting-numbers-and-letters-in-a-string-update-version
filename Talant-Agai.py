def count_letters_digits(text):
    letters = 0
    digits = 0
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits
def main():
    print("🔹 Программа подсчёта букв и цифр")
    print("Введите 'стоп' для выхода\n")