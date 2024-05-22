def laptop_info():
    laptops = {}
    with open('laptops.txt', 'r') as file:
        for line in file:
            name, brand, price, quantity, processor, graphics = line.strip().split(', ')
            price = float(price.strip('$'))
            quantity = int(quantity)
            laptops[name] = {
                'Brand Name': brand,
                'price': price,
                'quantity': quantity,
                'processor': processor,
                'graphics': graphics
            }
    return laptops

def display_stock():
    laptops = laptop_info()
    print("+----------------------------------------------------------------------------------------------------------------------+")
    print("+ S.N.\t|Name|\t\t  |Brand|\t\t|Price|\t\t|Quantity|\t|Processor|\t |Graphic Card|                      +")
    print("+----------------------------------------------------------------------------------------------------------------------+")
    SN = 1
    for name, specs in laptops.items():
        print(f"{SN}\t{name:<20}{specs['Brand Name']}\t\t${specs['price']}\t\t{specs['quantity']}\t\t{specs['processor']}\t{specs['graphics']}")
        SN += 1
    print("+-----------------------------------------------------------------------------------------------------------------------+")

def Selling_laptop():
    laptops = laptop_info()
    display_stock()
    selected_sn = input("Enter the serial number of the laptop you want: ")
    if not selected_sn.isdigit():
        print("Serial Number Can't be String")
        while not selected_sn.isdigit():
            print("Enter valid Input")
            selected_sn = input("Enter the serial number of the laptop you want: ")

    selected_sn = int(selected_sn)
    if selected_sn not in range(1, len(laptops) + 1):
        print("Error: Invalid serial number.")
        return

    user_name = input("Enter your name: ")
    laptop_name = list(laptops.keys())[selected_sn - 1]
    laptop = laptops[laptop_name]
    print(f"You Selected: {laptop_name}: nice choice")
    try:
        quantity = int(input("Enter the quantity of laptops you want to buy: "))
        if quantity < 1:
            print("Invalid quantity")
            return
    except ValueError:
        print('Quantity cannot contain alphabets')
        return

    if laptop['quantity'] < quantity:
        print(f"Error: Not enough {laptop_name} in stock to sell {quantity} units.")
        return

    laptop['quantity'] -= quantity
    total_price_without_shipping_cost = laptop['price'] * quantity
    shipping = input("Do you want shipment service? (yes/no): ").strip().upper()
    shipping_cost = 50 if shipping == "YES" else 0
    total_cost_with_shipping_cost = total_price_without_shipping_cost + shipping_cost
    invoice = f"""
    Invoice:
    Customer Name: {user_name}
    Laptop: {laptop_name}
    Quantity: {quantity}
    Total Price (without shipping): ${total_price_without_shipping_cost}
    Shipping Cost: ${shipping_cost}
    Total Cost: ${total_cost_with_shipping_cost}
    """
    print(invoice)
    with open("SALE_INVOICE.txt", "w") as file:
        file.write(invoice)
    print("Check txt file for invoice")

    with open('laptops.txt', 'w') as file:
        for name, details in laptops.items():
            file.write(f"{name}, {details['Brand Name']}, ${details['price']}, {details['quantity']}, {details['processor']}, {details['graphics']}\n")

def purchase_laptop():
    laptops = laptop_info()
    print("\t\t\t\t Laptop Stock : ")
    display_stock()
    name_of_distributor = input("Enter distributor name: ")
    laptop_name = input("Enter laptop name: ").upper()
    if laptop_name not in laptops:
        print("Laptop cannot be purchased")
        return
    laptop = laptops[laptop_name]
    try:
        quantity = int(input("Enter number of laptops: "))
        if quantity < 1:
            print("Invalid quantity")
            return
    except ValueError:
        print("Provide correct value")
        return

    total_prize_without_VAT = laptop['price'] * quantity
    VAT_amount = 0.13 * total_prize_without_VAT
    total_prize_with_VAT = VAT_amount + total_prize_without_VAT

    laptop['quantity'] += quantity
    invoice = f"""
    Invoice:
    Distributor Name: {name_of_distributor}
    Laptop: {laptop_name}
    Quantity: {quantity}
    Total Price (without VAT): ${total_prize_without_VAT}
    VAT Amount: ${VAT_amount}
    Total Price (with VAT): ${total_prize_with_VAT}
    """
    print(invoice)
    print("Your invoice has been generated in text file.")
    with open("purchase_invoice.txt", "w") as file:
        file.write(invoice)

    with open('laptops.txt', 'w') as file:
        for name, details in laptops.items():
            file.write(f"{name}, {details['Brand Name']}, ${details['price']}, {details['quantity']}, {details['processor']}, {details['graphics']}\n")

def choose_option():
    while True:
        print("\n\t***Welcome to Techtronics Traders\t")
        print("""
        Enter What you want to do.
        1 : Display Stock
        2 : Sale
        3 : Purchase
        4 : Exit Store
        """)
        option = input("Select an option: ")
        if option == '1':
            display_stock()
        elif option == '2':
            Selling_laptop()
        elif option == '3':
            purchase_laptop()
        elif option == '4':
            break
        else:
            try:
                int(option)
                print("Invalid option. Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Option number should be an integer.")
    
choose_option()
