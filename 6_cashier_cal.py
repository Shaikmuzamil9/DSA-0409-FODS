# Given data
item_prices = [2.5, 1.0, 3.0, 4.5]  # List of item prices
quantities = [3, 2, 1, 4]            # List of corresponding quantities
discount_rate = 10                  # Discount rate in percentage
tax_rate = 8                        # Tax rate in percentage

# Calculate the total cost before applying discount
total_cost_before_discount = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))

# Calculate the discount amount
discount_amount = (discount_rate / 100) * total_cost_before_discount

# Calculate the total cost after applying discount
total_cost_after_discount = total_cost_before_discount - discount_amount

# Calculate the tax amount
tax_amount = (tax_rate / 100) * total_cost_after_discount

# Calculate the final total cost including tax
final_total_cost = total_cost_after_discount + tax_amount

print("Total cost before discount:", total_cost_before_discount)
print("Discount amount:", discount_amount)
print("Total cost after discount:", total_cost_after_discount)
print("Tax amount:", tax_amount)
print("Final total cost:", final_total_cost)
