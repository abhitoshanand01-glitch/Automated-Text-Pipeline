import csv
import random

num_records = 250
filename = 'coffee_shop_data.csv'

genders = ['Male', 'Female', 'Non-Binary']
beverages = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Iced Coffee', 'Tea']

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['CustomerID', 'Age', 'Gender', 'Income_Monthly', 'Beverage_Type', 'Items_Bought', 'Spend_Amount', 'Satisfaction_Score', 'Loyalty_Member'])
    
    # Generate 250 random records
    for i in range(1, num_records + 1):
        customer_id = 1000 + i
        age = random.randint(18, 65)
        gender = random.choices(genders, weights=[45, 45, 10])[0]
        income = random.randint(15000, 90000)
        beverage = random.choice(beverages)
        items = random.randint(1, 4)
        
        # Calculate spend amount based on items bought
        base_spend = items * random.uniform(3.5, 6.5)
        spend = round(base_spend, 2)
        
        # Satisfaction score (1 to 5)
        satisfaction = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 20, 35, 30])[0]
        
        # Loyalty member (1 = Yes, 0 = No)
        loyalty = random.choices([0, 1], weights=[60, 40])[0] 
        
        writer.writerow([customer_id, age, gender, income, beverage, items, spend, satisfaction, loyalty])

print(f"Success! Generated {num_records} records in '{filename}'")