from bittrex import Bittrex
import requests

bittrex = Bittrex('', '')
BUY_ORDERBOOK = 'buy'
SELL_ORDERBOOK = 'sell'
BOTH_ORDERBOOK = 'both'
volume = []
lastdict = []

def greeting():
    print('--------------------------------------------------')
    print('Welcome to PumpChecker 1.0')
    print('--------------------------------------------------')

def coin():
    coin = input("What coin are you interested in pumping? ")
    return coin

def total_btc(quantity, rate):
    response = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc_price = data['bpi']['USD']['rate']
    btc_price = btc_price.replace(',', '')
    total = rate * quantity
    total_usd = (rate * float(btc_price)) * quantity
    return total, total_usd

def get_sells(coin):
    sells = bittrex.get_orderbook('BTC-{0}'.format(coin), SELL_ORDERBOOK)
    if sells['success'] is False:
        print(sells['message'])
    for sell in range(51):
        order = sells['result'][sell]
        quantity = order['Quantity']
        rate = order['Rate']
        if sell == 50:
            lastdict.append(rate)
        total, total_usd = total_btc(quantity, rate)
        volume.append(total)

def add_sells():
    all_btc = sum(volume)
    return float("{0:.3f}".format(all_btc))

def calc_multiplier(coin):
    last = lastdict[0]
    print(last)
    last_price = bittrex.get_ticker('BTC-{0}'.format(coin))['result']['Last']
    print(last_price)
    multiplier = last/last_price
    return float("{0:.3f}".format(multiplier))

def main(coin):
    #greeting()
    #coin = coin()
    get_sells(coin)
    all_btc = add_sells()
    multiplier = calc_multiplier(coin)
    #print('Total of {0}BTC to reach a {1}x multiplier'.format(all_btc, multiplier))
    return all_btc, multiplier
