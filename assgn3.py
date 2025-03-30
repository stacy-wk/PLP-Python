# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    # Check if discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount amount from original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return original price
        return price

# Prompt user to enter original price of the item
original_price = float(input("Enter the original price of the item: "))

# Prompt user to enter discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function to calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Check if original price was returned
if final_price == original_price:
    print("No discount. Original price:", original_price)
else:
    print("Final price after discount:", final_price)
