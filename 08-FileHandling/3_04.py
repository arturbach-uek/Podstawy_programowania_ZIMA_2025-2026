import re as regular_expressions

with open('report.txt', 'r', encoding='utf-8') as f:
    email = f.read()

pattern = r'\d+(?:[.,]\d+)?'

amounts = [float(money.replace(',', '.')) for money in regular_expressions.findall(pattern, email)]
total = sum(amounts)

print(f"Total spent: {total}")
