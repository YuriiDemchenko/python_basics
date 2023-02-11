text = input("Enter the text: ")
forbidden_letters = ["ы", "ъ", "ё", "э"]
if any(x in text for x in forbidden_letters):
    print("Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!")
else:
    print("Дякуємо за замовлення!")
