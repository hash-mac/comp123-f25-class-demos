# approach 1
print("=== approach 1 ====")
sname1 = "stock1"
sname2 = "stock2"
sname3 = "stock3"
sname4 = "stock4"
sname5 = "stock5"
sprice1 = 10
sprice2 = 20
sprice3 = 30
sprice4 = 40
sprice5 = 50
print(sname1 + ":" + str(sprice1))
print(sname2 + ":" + str(sprice2))
print(sname3 + ":" + str(sprice3))
print(sname4 + ":" + str(sprice4))
print(sname5 + ":" + str(sprice5))

# approach 2
print("=== approach 2 ====")
snames = ["stock1", "stock2", "stock3", "stock4", "stock5"]
sprices = [10, 20, 30, 40, 50]
for i in range(len(snames)):
    print(snames[i] + ":" + str(sprices[i]))

# approach 3
print("=== approach 3 ====")
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


# approach 4
print("=== approach 4 ====")
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

# approach 5
print("=== approach 5 ====")
Stocks = [
    Stock("stock1", 10),
    Stock("stock2", 20),
    Stock("stock3", 30),
    Stock("stock4", 40),
    Stock("stock5", 50)
]
for stock in Stocks:
    print(stock)
