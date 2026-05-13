# generators used for saving the memory

daily_sales = [5, 10, 12, 6, 7, 8, 11, 3]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)