import telegram_send
import yfinance as yf

btc = yf.Ticker("VGX-USD")

asset_data = btc.info

print(asset_data)

current_Price = round(asset_data['regularMarketPrice'],2)
market_Cap = round((int(asset_data['marketCap'])/1000000),2)

print(current_Price)

telegram_send.send(messages=["VGX Price is now ${} with a market cap of ${} Million".format(current_Price,market_Cap)])