class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price is $", self.__maxprice)

    def setmaxprice(self, price):
        self.__maxprice = price

c = computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# use setter function and display changed price
c.setmaxprice(1000)
c.sell()