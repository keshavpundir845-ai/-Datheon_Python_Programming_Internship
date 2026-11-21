# Task 2 - Stock Portfolio Tracker
# Datheon Python Programming Internship

portfolio = {}

# Sample stock prices (Live API ki jagah sample data use kiya hai)
STOCK_PRICES = {
    "AAPL": 195.50,
    "GOOGL": 175.20,
    "MSFT": 425.30,
    "TSLA": 248.90,
    "RELIANCE": 2450.75,
    "TCS": 3850.60,
    "INFY": 1520.40,
    "HDFC": 1650.25
}

def add_stock():
    symbol = input("Stock Symbol likho (jaise AAPL, TCS): ").upper()
    try:
        quantity = int(input("Kitne shares kharide? : "))
        buy_price = float(input("Kis price pe kharida? : "))
    except ValueError:
        print("Sahi number daalo!")
        return

    if symbol in portfolio:
        old_qty = portfolio[symbol]['quantity']
        old_total = portfolio[symbol]['quantity'] * portfolio[symbol]['buy_price']
        new_total = old_total + (quantity * buy_price)
        portfolio[symbol]['quantity'] = old_qty + quantity
        portfolio[symbol]['buy_price'] = new_total / portfolio[symbol]['quantity']
    else:
        portfolio[symbol] = {'quantity': quantity, 'buy_price': buy_price}
    
    print(f"\n✅ {quantity} shares of {symbol} add ho gaye!")

def view_portfolio():
    if not portfolio:
        print("\nPortfolio khaali hai! Pehle stock add karo.")
        return

    print("\n" + "="*70)
    print("YOUR STOCK PORTFOLIO".center(70))
    print("="*70)
    print(f"{'Stock':<10} {'Qty':<8} {'Buy Price':<12} {'Current':<12} {'P/L':<12}")
    print("-"*70)

    total_invested = 0
    total_current = 0

    for symbol, data in portfolio.items():
        qty = data['quantity']
        buy = data['buy_price']
        current = STOCK_PRICES.get(symbol, buy)  # Agar price na mile to buy price hi
        invested = qty * buy
        current_val = qty * current
        profit = current_val - invested

        total_invested += invested
        total_current += current_val

        print(f"{symbol:<10} {qty:<8} ₹{buy:<11.2f} ₹{current:<11.2f} ₹{profit:<11.2f}")

    print("-"*70)
    total_profit = total_current - total_invested
    print(f"Total Invested: ₹{total_invested:.2f}")
    print(f"Total Current Value: ₹{total_current:.2f}")
    print(f"Total Profit/Loss: ₹{total_profit:.2f}")
    if total_invested > 0:
        print(f"Return %: {(total_profit/total_invested)*100:.2f}%")
    print("="*70)

def remove_stock():
    symbol = input("Kaunsa stock hatana hai? Symbol likho: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"✅ {symbol} hata diya gaya!")
    else:
        print("Ye stock portfolio me nahi hai!")

def main():
    print("="*50)
    print("  STOCK PORTFOLIO TRACKER - Task 2")
    print("  Datheon Python Internship")
    print("="*50)
    print("Available Stocks:", ", ".join(STOCK_PRICES.keys()))

    while True:
        print("\n--- MENU ---")
        print("1. Stock Add Karo")
        print("2. Portfolio Dekho")
        print("3. Stock Hatao")
        print("4. Exit")
        
        choice = input("Apna choice likho (1-4): ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            remove_stock()
        elif choice == "4":
            print("\nThanks! Portfolio Tracker band ho raha hai.")
            break
        else:
            print("Galat choice! 1-4 me se chuno.")

if __name__ == "__main__":
    main()
