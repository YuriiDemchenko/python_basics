car_price_eu = 6500
exchange_rate = float(input("Курс євро до гривні: "))
sum_uah = int(input("Сума в грн: "))
car_count = (sum_uah / exchange_rate) // car_price_eu
print("Кількість бандеромобілів: " , car_count)