from yfinance import Ticker

tk = Ticker("GOOG")

data = tk.history("max")
