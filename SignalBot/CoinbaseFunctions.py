import ccxt
import config

"""
# COINBASE COMMANDS
# Place a market buy order
#order = coinbase.create_market_buy_order(symbol, usd_amount)

#place a market sell
#sell_order = coinbase.create_market_sell_order(symbol, cc_amount)

#fetch and print balance
# balance = coinbase.fetch_balance()
"""


# Initialize the Coinbase exchange
def initialize_coinbase():
    return ccxt.coinbase({
        'apiKey': config.api_key,
        'secret': config.api_secret,
        'enableRateLimit': True,
        'options': {
            'createMarketBuyOrderRequiresPrice': False,
        },
    })



"""
# need a function that can get our current liquid account balance in dollars
    # this function will then reutrn a percentage of that balance and we will call that a unit
    #so unit should have type double or float since it is money
    # unit will be passed as a prameter into coinbase_buy
"""

def get_unit(coinbase_exchange):
    balance =  coinbase_exchange.fetch_balance()
    usd_balance = balance['free']['USD']
    unit = usd_balance * .2
    return unit

"""
# to sell our position we need to say how much crypto we want to sell
# this is different than buying where we specify how much USD we want to spend 
# thus we need a function that can get our current position ie how much crypto have we invested
    # rn lets just get the entire position and use that; maybe later we can do fancy hedging
    # this function will then return that exact value 
    # we will call this current_holdings, should be of type double or float since it is a number
    # current_holdings will be passed as a parameter into coinbase_sell 
"""

def get_current_holdings(coinbase_exchange, symbol): 
    balance = coinbase_exchange.fetch_balance()
    holdings = {currency: amounts for currency, amounts in balance['total'].items()}
    holdings = holdings[symbol]
    return holdings



def coinbase_buy(dummyvar, unit): #coinbase_buy(symbol, ... , unit)
    try:
        #order = coinbase.create_market_buy_order(symbol, ..., unit)
        print(f"Market BUY: {dummyvar}")
        print(f"Unit:{unit}")
        #return something signaling a purchase
    except ccxt.BaseError as e:
        print(f"An error occurred: {e}")    
        #return something signaling a failed purchase

def coinbase_sell(dummyvar, holdings): #coinbase_sell(symbol, holdings)
    try:
        #sell_order = coinbase.create_market_sell_order(symbol, holdings)
        print(f"market SELL:{dummyvar}")
        print(f"holdings:{holdings}")
        #return something signaling a purchase
    except ccxt.BaseError as e:
        print(f"An error occurred: {e}")    
        #return something signaling a failed sell