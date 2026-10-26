# Investment Portfolio Tracking Utility
A Python-based investment portfolio tracking utility designed for the Datheon Python Programming Internship.

## Features
- **Ticker Validation:** Validates stock tickers against the S&P 500 constituents database (`constituents.csv`).
- **Position Tracking:** Tracks ticker symbol, company name, purchase price, current price, shares quantity, and invested capital.
- **Financial Calculations:**
  - Total Invested Capital
  - Current Portfolio Value
  - Absolute Gain/Loss ($)
  - Percentage Gain/Loss (%)
- **CSV Export:** Automatically logs transaction and holding summaries to `portfolio_summary.csv` using Python's standard `csv` module.
- **Robust Price Fetching:** Attempts live market price lookup with an offline fallback.

## Requirements
- Python 3.8+
- (Optional for live data) `yfinance` or `requests` (Standard library `urllib` is used by default with offline fallback).

## How to Run
```bash
python portfolio.py
```
