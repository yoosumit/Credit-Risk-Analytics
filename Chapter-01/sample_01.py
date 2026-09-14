# Employee 1 → ₹12,000
# Employee 2 → ₹15,000
# Employee 3 → ₹9,000
# Employee 4 → ₹18,000
# Employee 5 → ₹11,000


emp_sales = [12000, 15000, 9000, 18000, 11000]
sales_total = sum(emp_sales)
avg = sales_total / len(emp_sales)
highest = max(emp_sales)
lowest = min(emp_sales)

print( sales_total, avg, highest, lowest)
