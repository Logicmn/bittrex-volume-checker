from bittrex import Bittrex
import requests

bittrex = Bittrex('', '')
BUY_ORDERBOOK = 'buy'
SELL_ORDERBOOK = 'sell'
BOTH_ORDERBOOK = 'both'

def total_btc(quantity, rate):
    total = rate * quantity
    return total

def get_sells(coin, desired_multiplier):
    volume = []
    sells = bittrex.get_orderbook('BTC-{0}'.format(coin), SELL_ORDERBOOK)
    if sells['success'] is False:
        print(sells['message'], '#########################################################')
    for sell in range(1000):
        order = sells['result'][sell]
        quantity = order['Quantity']
        rate = order['Rate']
        total = total_btc(quantity, rate)
        volume.append(total)
        last_price = bittrex.get_ticker('BTC-{0}'.format(coin))['result']['Last']
        multiplier = rate / last_price
        multiplier = float("{0:.1f}".format(multiplier))
        if multiplier != desired_multiplier:
            continue
        else:
            return volume, rate, last_price
