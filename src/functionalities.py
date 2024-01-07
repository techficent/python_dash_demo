from typing import List,Callable
from pandas import DataFrame
from yfinance import Ticker

def show_menu() -> None :
    msg_string = """Enter 1 for info\n2 for statistical description\n3 for missing values count\n
4 for head\n5 for tail\n6 for all of the above\n"""
    choice = int ( input(msg_string) )
    return choice


"""
    This function should display basic exploratory data analytics
    info
"""

def explore_data(data : DataFrame) -> None :
    
    operations : List[Callable] = [data.describe, data.isna().sum, data.head, data.tail]

    choice = (show_menu())
    choice = show_menu
    if choice in [4,5]:
        n = int ( input("Enter count of rows to be displayed\t") )
        print ( operations[-1 + (show_menu())](n) )
    elif choice == 1:
        data.info()
    elif choice in [2,3] :
        print ( operations[-1 + (show_menu())]() )
    elif choice == 6 :
        data.info()
        for fn in operations:
            print(fn())
    else :
        raise ValueError("Invalid choice")

"""
    This function fetches data from the yfinance api for ticker_name passed
"""

def fetch_data() -> DataFrame :
    ticker_name = input("Enter a ticker name (use .NS for NSE listed stocks): ")

    tk = Ticker(ticker_name)

    data = tk.history("max")

    print(data.sample(3))

    explore_data(data)

    return data
    
"""
main app start function
"""    
def main() -> None:
    fetch_data()
