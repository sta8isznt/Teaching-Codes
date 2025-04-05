sales = {
    "ηλεκτρονικά": [100, 200, 300],
    "ρούχα": [50, 30, 50],
    "τρόφιμα": [20, 30, 40, 60]
}

total_sales = 0
for cat, prices in sales.items():
    total_sales += sum(prices)

print(total_sales)

best_cat = "ηλεκτρονικά"
best_cat_ammount = sum(sales["ηλεκτρονικά"])
for cat, prices in sales.items():
    if sum(prices) > best_cat_ammount:
        best_cat = cat
        best_cat_ammount = sum(prices)
print(best_cat, best_cat_ammount)