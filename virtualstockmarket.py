import random

class StockMarket:
    def __init__(self):
        self.stocks = {"AAPL": 150, "GOOGL": 2800, "AMZN": 3500, "TSLA": 900}
        self.user_portfolio = {}

    def display_stocks(self):
        print("\nCurrent Stock Prices:")
        for stock, price in self.stocks.items():
            print(f"{stock}: ${price}")

    def update_prices(self):
        for stock in self.stocks:
            change = random.uniform(-0.05, 0.05)  # Random price change
            self.stocks[stock] += self.stocks[stock] * change
            self.stocks[stock] = round(self.stocks[stock], 2)

    def buy_stock(self, stock, quantity):
        if stock in self.stocks:
            cost = self.stocks[stock] * quantity
            if stock in self.user_portfolio:
                self.user_portfolio[stock] += quantity
            else:
                self.user_portfolio[stock] = quantity
            print(f"Bought {quantity} shares of {stock} for ${cost:.2f}")
        else:
            print("Stock not found.")

    def sell_stock(self, stock, quantity):
        if stock in self.user_portfolio and self.user_portfolio[stock] >= quantity:
            revenue = self.stocks[stock] * quantity
            self.user_portfolio[stock] -= quantity
            if self.user_portfolio[stock] == 0:
                del self.user_portfolio[stock]
            print(f"Sold {quantity} shares of {stock} for ${revenue:.2f}")
        else:
            print("Not enough shares to sell or stock not in portfolio.")

    def display_portfolio(self):
        print("\nYour Portfolio:")
        if not self.user_portfolio:
            print("No stocks owned.")
        else:
            for stock, quantity in self.user_portfolio.items():
                value = self.stocks[stock] * quantity
                print(f"{stock}: {quantity} shares, Value: ${value:.2f}")

def main():
    market = StockMarket()
    while True:
        market.display_stocks()
        print("\nOptions: 1. Buy Stock 2. Sell Stock 3. View Portfolio 4. Next Day 5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            stock = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            market.buy_stock(stock, quantity)
        elif choice == "2":
            stock = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            market.sell_stock(stock, quantity)
        elif choice == "3":
            market.display_portfolio()
        elif choice == "4":
            market.update_prices()
        elif choice == "5":
            print("Exiting the simulation. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
