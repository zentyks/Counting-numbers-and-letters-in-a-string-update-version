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
    while True:
        try:
            user_input = input("Введите строку: ").strip()
            if user_input.lower() == "стоп":
                print("Выход из программы 👋")
                break
            letters, digits = count_letters_digits(user_input)
            print("\n📊 Результат:")
            print(f"Буквы: {letters}")
            print(f"Цифры: {digits}")
            print("-" * 30)
        except Exception as e:
            print("Ошибка ввода! Попробуйте снова.")
if __name__ == "__main__":
    main()