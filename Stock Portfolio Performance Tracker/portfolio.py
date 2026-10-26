"""
Investment Portfolio Tracking Utility
Program: Python Programming Internship
File: portfolio.py
Description:
    A utility script to track stock portfolio positions, compute
    investment metrics (total invested capital, current value, gain/loss percentage),
    and log the transaction summary into an external CSV file.
"""

import csv
import json
import os
import sys
import urllib.request
import urllib.error


CONSTITUENTS_FILE = "constituents.csv"
OUTPUT_SUMMARY_FILE = "portfolio_summary.csv"


def load_sp500_constituents(file_path=CONSTITUENTS_FILE):
    """
    Load S&P 500 tickers and company names from CSV into a dictionary.
    Returns: dict mapping symbol to security name (e.g. {'AAPL': 'Apple Inc.'})
    """
    companies = {}
    if not os.path.exists(file_path):
        return companies

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                symbol = row.get("Symbol", "").strip().upper()
                security = row.get("Security", "").strip()
                if symbol:
                    companies[symbol] = security
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")

    return companies


def fetch_current_price(ticker):
    """
    Attempt to fetch the latest market price for a given ticker.
    Uses Yahoo Finance chart API. Returns None if lookup fails or offline.
    """
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )

    try:
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode("utf-8"))
            meta = data["chart"]["result"][0]["meta"]
            price = meta.get("regularMarketPrice")
            if price is not None:
                return float(price)
    except Exception:
        # Fallback to manual entry if request fails
        pass

    return None


def get_float_input(prompt, min_val=0.0):
    """Prompt user for a valid positive floating point number."""
    while True:
        try:
            val = float(input(prompt).strip())
            if val <= min_val:
                print(f"Value must be greater than {min_val}. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int_input(prompt, min_val=1):
    """Prompt user for a valid integer quantity."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val < min_val:
                print(f"Quantity must be at least {min_val}. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_portfolio_metrics(portfolio):
    """
    Compute metrics for each holding and total portfolio values:
    - Invested Capital = buy_price * quantity
    - Current Market Value = current_price * quantity
    - Gain/Loss ($) = current_value - invested_capital
    - Gain/Loss (%) = (gain_loss / invested_capital) * 100
    """
    total_invested = 0.0
    total_current_val = 0.0

    for symbol, pos in portfolio.items():
        qty = pos["quantity"]
        buy_price = pos["buy_price"]
        current_price = pos["current_price"]

        invested = qty * buy_price
        current_val = qty * current_price
        gain_loss = current_val - invested
        gain_loss_pct = (gain_loss / invested * 100) if invested > 0 else 0.0

        pos["invested_capital"] = invested
        pos["current_value"] = current_val
        pos["gain_loss"] = gain_loss
        pos["gain_loss_pct"] = gain_loss_pct

        total_invested += invested
        total_current_val += current_val

    total_gain_loss = total_current_val - total_invested
    total_gain_loss_pct = (total_gain_loss / total_invested * 100) if total_invested > 0 else 0.0

    return {
        "total_invested": total_invested,
        "total_current_val": total_current_val,
        "total_gain_loss": total_gain_loss,
        "total_gain_loss_pct": total_gain_loss_pct
    }


def display_portfolio(portfolio, summary):
    """Print a clean formatted summary table to the console."""
    if not portfolio:
        print("\nPortfolio is currently empty.")
        return

    print("\n" + "=" * 98)
    print(f"{'INVESTMENT PORTFOLIO SUMMARY':^98}")
    print("=" * 98)
    header = f"{'Symbol':<7} | {'Company Name':<25} | {'Qty':>5} | {'Buy ($)':>9} | {'Cur ($)':>9} | {'Invested ($)':>13} | {'Value ($)':>13} | {'P/L (%)':>8}"
    print(header)
    print("-" * 98)

    for symbol, pos in portfolio.items():
        comp_name = pos.get("company_name", "N/A")[:25]
        qty = pos["quantity"]
        buy_p = pos["buy_price"]
        cur_p = pos["current_price"]
        inv = pos["invested_capital"]
        cur_v = pos["current_value"]
        pct = pos["gain_loss_pct"]

        pct_str = f"{pct:+.2f}%"
        print(f"{symbol:<7} | {comp_name:<25} | {qty:>5} | {buy_p:>9.2f} | {cur_p:>9.2f} | {inv:>13.2f} | {cur_v:>13.2f} | {pct_str:>8}")

    print("-" * 98)
    print(f"Total Invested Capital : ${summary['total_invested']:,.2f}")
    print(f"Total Current Value    : ${summary['total_current_val']:,.2f}")
    pl_sign = "+" if summary['total_gain_loss'] >= 0 else ""
    print(f"Total Portfolio Return : {pl_sign}${summary['total_gain_loss']:,.2f} ({summary['total_gain_loss_pct']:+.2f}%)")
    print("=" * 98 + "\n")


def export_summary_to_csv(portfolio, summary, output_file=OUTPUT_SUMMARY_FILE):
    """Write the portfolio summary and holdings to a CSV file."""
    fieldnames = [
        "Ticker",
        "Company Name",
        "Quantity",
        "Buy Price ($)",
        "Current Price ($)",
        "Invested Capital ($)",
        "Current Market Value ($)",
        "Gain/Loss ($)",
        "Gain/Loss (%)"
    ]

    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for symbol, pos in portfolio.items():
                writer.writerow({
                    "Ticker": symbol,
                    "Company Name": pos.get("company_name", "N/A"),
                    "Quantity": pos["quantity"],
                    "Buy Price ($)": f"{pos['buy_price']:.2f}",
                    "Current Price ($)": f"{pos['current_price']:.2f}",
                    "Invested Capital ($)": f"{pos['invested_capital']:.2f}",
                    "Current Market Value ($)": f"{pos['current_value']:.2f}",
                    "Gain/Loss ($)": f"{pos['gain_loss']:+.2f}",
                    "Gain/Loss (%)": f"{pos['gain_loss_pct']:+.2f}%"
                })

            # Append the total portfolio summary row
            writer.writerow({
                "Ticker": "TOTAL",
                "Company Name": "---",
                "Quantity": sum(p["quantity"] for p in portfolio.values()),
                "Buy Price ($)": "---",
                "Current Price ($)": "---",
                "Invested Capital ($)": f"{summary['total_invested']:.2f}",
                "Current Market Value ($)": f"{summary['total_current_val']:.2f}",
                "Gain/Loss ($)": f"{summary['total_gain_loss']:+.2f}",
                "Gain/Loss (%)": f"{summary['total_gain_loss_pct']:+.2f}%"
            })

        print(f"[OK] Summary successfully saved to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to CSV: {e}")


def load_sample_portfolio(portfolio, sp500_data):
    """Load default sample positions for testing."""
    samples = [
        ("AAPL", 150.00, 10, 185.50),
        ("MSFT", 310.00, 5, 425.00),
        ("NVDA", 450.00, 8, 880.00),
        ("AMZN", 130.00, 12, 180.00),
        ("TSLA", 240.00, 6, 215.00),
    ]

    for sym, buy, qty, cur in samples:
        portfolio[sym] = {
            "company_name": sp500_data.get(sym, sym),
            "buy_price": buy,
            "quantity": qty,
            "current_price": cur
        }
    print("[OK] Loaded 5 sample stock positions.")


def main():
    print("=" * 65)
    print("       INVESTMENT PORTFOLIO TRACKING UTILITY")
    print("=" * 65)

    # Load S&P 500 constituents
    sp500_data = load_sp500_constituents()
    if sp500_data:
        print(f"[Info] Loaded {len(sp500_data)} tickers from {CONSTITUENTS_FILE}.")
    else:
        print(f"[Info] {CONSTITUENTS_FILE} not found. Running with direct ticker inputs.")

    # Dictionary to hold portfolio positions
    portfolio = {}

    while True:
        print("\nMain Menu:")
        print("1. Add Stock Position")
        print("2. Load Sample Portfolio")
        print("3. View Portfolio & Export CSV")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            ticker = input("\nEnter Stock Ticker (e.g. AAPL, MSFT, GOOGL): ").strip().upper()
            if not ticker:
                print("Ticker cannot be blank.")
                continue

            company_name = sp500_data.get(ticker, ticker)
            print(f"Company: {company_name}")

            buy_price = get_float_input(f"Enter buy price per share ($) for {ticker}: ")
            quantity = get_int_input(f"Enter number of shares for {ticker}: ")

            print(f"Checking current price for {ticker}...")
            current_price = fetch_current_price(ticker)
            if current_price:
                print(f"[OK] Live market price: ${current_price:.2f}")
            else:
                print("Live price unavailable. Please enter current price manually.")
                current_price = get_float_input(f"Enter current market price ($) for {ticker}: ")

            portfolio[ticker] = {
                "company_name": company_name,
                "buy_price": buy_price,
                "quantity": quantity,
                "current_price": current_price
            }
            print(f"[OK] {ticker} added to portfolio.")

        elif choice == "2":
            load_sample_portfolio(portfolio, sp500_data)

        elif choice == "3":
            if not portfolio:
                print("Portfolio is empty. Please add positions first.")
                continue
            summary = calculate_portfolio_metrics(portfolio)
            display_portfolio(portfolio, summary)
            export_summary_to_csv(portfolio, summary)

        elif choice == "4":
            if portfolio:
                summary = calculate_portfolio_metrics(portfolio)
                export_summary_to_csv(portfolio, summary)
            print("\nExiting Investment Portfolio Tracker. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose an option between 1 and 4.")


if __name__ == "__main__":
    main()
