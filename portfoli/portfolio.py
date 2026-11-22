
import csv
import os
from datetime import datetime

# Sample current stock prices
# Update these values with current market prices
current_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 1400,
    "HDFC": 1700,
    "WIPRO": 250
}

# Store portfolio details
portfolio = {}

print("\n================================")
print("   INVESTMENT PORTFOLIO TRACKER")
print("================================")

n = int(input("\nEnter number of stocks: "))

for i in range(n):

    print("\nStock", i + 1)

    ticker = input("Enter stock symbol: ").upper()

    if ticker in portfolio:
        print("Stock already entered! Use another symbol.")
        continue

    buy_price = float(input("Enter buying price: "))
    quantity = int(input("Enter quantity: "))

    if buy_price <= 0 or quantity <= 0:
        print("Price and quantity must be positive!")
        continue

    # Get current stock price
    if ticker in current_prices:
        market_price = current_prices[ticker]
    else:
        market_price = float(
            input("Enter current market price: ")
        )

    if market_price <= 0:
        print("Market price must be positive!")
        continue

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": market_price
    }


# Portfolio calculations
total_investment = 0
total_value = 0

print("\n========== PORTFOLIO SUMMARY ==========")

for ticker, details in portfolio.items():

    buy_price = details["buy_price"]
    quantity = details["quantity"]
    current_price = details["current_price"]

    invested = buy_price * quantity
    market_value = current_price * quantity

    profit_loss = market_value - invested

    percentage = (profit_loss / invested) * 100

    total_investment += invested
    total_value += market_value

    print("\nStock:", ticker)
    print("Buy Price:", buy_price)
    print("Quantity:", quantity)
    print("Current Price:", current_price)
    print("Invested Amount:", round(invested, 2))
    print("Market Value:", round(market_value, 2))
    print("Profit/Loss:", round(profit_loss, 2))
    print("Gain/Loss Percentage:", round(percentage, 2), "%")


# Overall portfolio summary
total_profit_loss = total_value - total_investment

if total_investment > 0:
    total_percentage = (
        total_profit_loss / total_investment
    ) * 100
else:
    total_percentage = 0

print("\n========== TOTAL PORTFOLIO ==========")

print("Total Investment:", round(total_investment, 2))
print("Current Value:", round(total_value, 2))
print("Total Profit/Loss:", round(total_profit_loss, 2))
print("Overall Percentage:", round(total_percentage, 2), "%")


# Save report to CSV
filename = "portfolio_summary.csv"

file_exists = os.path.isfile(filename)

with open(filename, "a", newline="") as file:

    writer = csv.writer(file)

    if not file_exists or os.path.getsize(filename) == 0:
        writer.writerow([
            "Date",
            "Stock",
            "Buy Price",
            "Quantity",
            "Current Price",
            "Investment",
            "Market Value",
            "Profit/Loss",
            "Percentage"
        ])

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for ticker, details in portfolio.items():

        buy = details["buy_price"]
        qty = details["quantity"]
        current = details["current_price"]

        investment = buy * qty
        value = current * qty
        profit = value - investment
        percent = (profit / investment) * 100

        writer.writerow([
            date,
            ticker,
            buy,
            qty,
            current,
            investment,
            value,
            round(profit, 2),
            round(percent, 2)
        ])

print("\nPortfolio report saved successfully!")
print("File name:", filename)
