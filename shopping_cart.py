print("---WELCOME TO BHATBHATENI SUPERMARKET---")

shop_items = {
    "grocery": {
        "chocolate": 150,
        "banana": 100,
        "flour": 120,
        "milk": 45,
        "bread": 60,
        "eggs": 600,
        "cheese": 320
    },
    "cosmetics": {
        "eye shadow": 250,
        "foundation": 30,
        "lipgloss": 80,
        "lotion": 200,
        "lipstick": 500
    },
    "electronics": {
        "phone": 15000,
        "laptop": 50000,
        "headphones": 1500,
        "charger": 500,
        "smartwatch": 3000
    }
}

budget = float(input("Enter your budget: "))

cart = []
total_cost = 0.0

while True:
    section_choice = input("Which section would you like to shop in? (grocery, cosmetics, electronics): ").strip().lower()

    if section_choice in shop_items:
        while True:
            print(f"\nAvailable items in {section_choice.capitalize()}:")
            for item, price in shop_items[section_choice].items():
                print(f"{item}: Rs.{price}")

            shopping_list = input("\nEnter your shopping list (comma separated): ").split(",")

            for item in shopping_list:
                item = item.strip()  
                if item in shop_items[section_choice]:
                    price = shop_items[section_choice][item]
                    if total_cost + price <= budget:
                        cart.append(item)
                        total_cost += price
                        print(f"Added {item} to the cart. Current total: Rs.{total_cost:.2f}")
                    else:
                        print(f"Cannot add {item}. Total would exceed budget of Rs.{budget:.2f}.")
                else:
                    print(f"{item} is not available in the {section_choice} section.")

            continue_shopping = input("\nDo you want to continue shopping in this section or switch to another section? (continue/switch): ").strip().lower()
            if continue_shopping == 'switch':
                break  
    else:
        print("Invalid section selected. Please choose a valid section.")

    if continue_shopping == 'switch':
        continue_shopping = input("\nDo you want to continue shopping in another section? (yes/no): ").strip().lower()
        if continue_shopping != 'yes':
            break  

print("\nItems in your cart:")
for item in cart:
    print(item)

print(f"Total cost: Rs.{total_cost:.2f}")
if total_cost <= budget:
    print("You are within your budget!")
else:
    print("You have exceeded your budget!")