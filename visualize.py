
import matplotlib.pyplot as plt

def buy_sell_plot(symbol: str, data):
    plt.style.use('fivethirtyeight')
    # visualize moving averages
    plt.figure(figsize=(10, 5))
    plt.title(symbol + ' Buy/Sell w/ 3 Moving Averages')
    plt.plot(data['4. close'], label='Close Price', color='blue', alpha=0.3)
    plt.plot(data['Short'], label='Short EMA', color='red', alpha=0.3)
    plt.plot(data['Middle'], label='Mid EMA', color='green', alpha=0.3)
    plt.plot(data['Long'], label='Long EMA', color='orange', alpha=0.3)
    plt.scatter(data.index, data['Buy'], color='green', marker='^', alpha=1)
    plt.scatter(data.index, data['Sell'], color='red', marker='v', alpha=1)

    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.show()