# Start Option and Greetings
print(" Write start to continue")
while True:
    user_input = input().lower()
    if user_input == "start":
        print("\nWelcome to Virtual Pizza Robot! We promise we won't judge you by your weird choices.")
        print("\nNow let's start to create your order.")
        break
else:
    print("PLease write start to continue")

# Get Customer Name
print("What is your name? ")
while True:
    name = input().strip()   #strip() to remove extra space
    if name.isalpha():
        name = name.capitalize()
        break
    else:
        print("Please enter a valid name using alphabets.")


# Vegetarian or Non-Vegetarian
print("\nWhat type of Pizza are you craving for?")
print("1. Veggie Pizza(for the health conscious)")
print("2.non-veggie(for the carnivores)")
user_choice = input().strip()
while user_choice not in ["1", "2"]:
    print("Oops!Please choose 1 or 2")
    user_choice = input().strip()
if user_choice == '1':
    print("Great Choice! You are going for a veggie Pizza.")
else:
    print("Yum! A meaty Pizza for you.")

# Pizza Size Selection
print("\nWhat size of pizza would you like?")
print("1. Small: Rs300 \n2. Extra Small: Rs 200 \n3. Only One Piece: Rs 100")
size_price = {'1': 300,'2':'200','3':100}
size = input("Enter your choice").strip()
while size not in ['1','2','3']:
    print("Enter the valid choice (1,2,3).")
    size = input("What size of Pizza would you like? ").strip()
select_sizeprice = size_price[size]

# Toppings Selection
print("\nChoose your toppings:")
print('''
      1. Extra Air Rs 50/-
      2. Invisible Cheese Rs 150/-
      3. Chocolate Chips  Rs 70/-
      4. Spicy Ice Cubes  Rs 30/-
      5. Banana Slices    Rs 40/-
      6. Popcorn  Rs 80/-
      7. Cotton Candy  Rs 250/-
      ''')
valid_choice = ['1','2','3','4','5','6','7']
topping_price = {'1':50,'2':150,'3':70,'4':30,'5':40,'6':80,'7':250}
while True:
    toppings = input("Enter atleast your Three favourite Toppings.").strip()
    if ',' in toppings:
        toppings = toppings.split()
    else:
        toppings = list(toppings)
    if all(choice in valid_choice for choice in toppings) and len (toppings) >= 3:
        break
    else:
        print("Invalid choice! Enter atleast your Three favourite Toppings.")
select_toppingprice = sum(topping_price[choice] for choice in toppings)

# give compliment
print("\n eww! weird choice, But we promise so we won't judge.")

# Cold Drink Selection
print("\nWould you like a cold drink with your order?")
print('''
      1. Choco Cola  Rs 120/-
      2. Blood Sting Rs 150/-
      3. Green Tea   Rs 50/-
      4. Nothing      Rs 0/-
      ''')
drink_price = {'1':120,'2':150,'3':50,'4':0}
choice = ['1','2','3','4']
while True:
    drink = input("Enter your favourite drink: ").strip()
    if drink  in choice:
        break
    else:
        print("Enter a valid choice using (1,2,3,4)")
select_drinkprice = drink_price[drink]

# total bill
total_pizzaprice = select_sizeprice + select_toppingprice + select_drinkprice
print(f"Your total bill is{total_pizzaprice}")

# Discount offer
print("\nThank you for your order! But wait, you might get a discount!")
print("Answer the following question to win your discount:")
print("What is the correct answer to this question: 'What is 2+2?'")
print("1. 4 \n2. 22 \n3. A pair of swans")

answer = input("Enter your choice (1, 2, or 3): ").strip()
if answer == "1":
    discount = 50  
    print("\nCorrect! You're a genius! You get Rs 50/- off.")
elif answer == "2":
    discount = 20  
    print("\nOh no, you're a little off, but that's okay! Here's Rs 20/- off.")
elif answer == "3":
    discount = 30  # 
    print("\nHmm, creative answer! You win Rs 30/- off.")
else:
    discount = 0  
    print("\nOops! Invalid answer. No discount for you this time.")

# Apply Discount
final_cost = total_pizzaprice - discount

# Order Confirmation Message
print("\nThank you for your order! \nDon’t worry, your pizza will arrive virtually on time.")