categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
index = expenses.index(max_expense)
most_expensive_category = categories[index]

print("Most expensive category:", most_expensive_category)
print("Amount:", max_expense)
