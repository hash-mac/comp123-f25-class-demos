def print_header(header):
    print()
    print("="*3, header, "="*3)


# approach 1: 1 var/name & 1 var/price
print_header("approach 1: 1 var/name & 1 var/price")
name1 = "stock1"
name2 = "stock2"
name3 = "stock3"
name4 = "stock4"
name5 = "stock5"
price1 = 10
price2 = 20
price3 = 30
price4 = 40
price5 = 50
print(name1 + ":" + str(price1))
print(name2 + ":" + str(price2))
print(name3 + ":" + str(price3))
print(name4 + ":" + str(price4))
print(name5 + ":" + str(price5))

# approach 2: list for names & list for prices
print_header("approach 2: list for names & list for prices")
names = ["stock1", "stock2", "stock3", "stock4", "stock5"]
prices = [10, 20, 30, 40, 50]
for i in range(len(names)):
    print(names[i] + ":" + str(prices[i]))

# approach 3: list of dictionaries (1 dict/stock)
print_header("approach 3: list of dictionaries (1 dict/stock)")
stocks = [
    {"name": "stock1", "price": 10},
    {"name": "stock2", "price": 20},
    {"name": "stock3", "price": 30},
    {"name": "stock4", "price": 40},
    {"name": "stock5", "price": 50},
]
for stock in stocks:
    print(stock["name"] + ":" + str(stock["price"]))


class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ":" + str(self.price)


# approach 4: 1 var/stock
print_header("approach 4: 1 var/stock")
stock1 = Stock("stock1", 10)
stock2 = Stock("stock2", 20)
stock3 = Stock("stock3", 30)
stock4 = Stock("stock4", 40)
stock5 = Stock("stock5", 50)

print(stock1)
print(stock2)
print(stock3)
print(stock4)
print(stock5)

# approach 5: list of stocks
print_header("approach 5: list of stocks")
Stocks = [
    Stock("stock1", 10),
    Stock("stock2", 20),
    Stock("stock3", 30),
    Stock("stock4", 40),
    Stock("stock5", 50)
]
for stock in Stocks:
    print(stock)
