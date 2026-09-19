stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:

    price = stock_prices[stock_name]
    total = price * quantity

    print("\n----- Stock Portfolio -----")
    print("Stock:", stock_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total)

else:
    print("Stock not found.")
