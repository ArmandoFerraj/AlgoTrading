import DontShare as cb
import ccxt

coinbase = ccxt.coinbase({
    'apiKey':cb.api_key,
    'secret':cb.api_secret,
    'enableRateLimit': True,
})

balance = coinbase.fetch_balance()
print(balance)




