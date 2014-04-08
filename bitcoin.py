import json
import urllib2
import webapp2

from google.appengine.api import urlfetch

class BitCoinPrice:
  buy_url = 'https://coinbase.com/api/v1/prices/buy'
  sell_url = 'https://coinbase.com/api/v1/prices/sell'

  def get_buy_price(self):
    output = urlfetch.fetch(self.buy_url)
    price, total_price = self.parse_buy_price(output.content)
    return price, total_price

  def get_sell_price(self):
    output = urlfetch.fetch(self.sell_url)
    price, total_price = self.parse_sell_price(output.content)
    return price, total_price

  def parse_buy_price(self, output):
    j = json.loads(output)
    price = j['subtotal']['amount']
    total_price = j['total']['amount']
    return price, total_price

  def parse_sell_price(self, output):
    j = json.loads(output)
    price = j['subtotal']['amount']
    total_price = j['total']['amount']
    return price, total_price


class MainPage(webapp2.RequestHandler):

  def get(self):
    bit_coin_price = BitCoinPrice()
    buy_price, total_buy_price = bit_coin_price.get_buy_price()
    sell_price, total_sell_price = bit_coin_price.get_sell_price()
    self.response.headers['Content-Type'] = 'text/plain'
    output = 'Buy price for 1 bit coin is %s, total buy price is %s.\nSell price for 1 bit coin is %s, total sell price is %s.' % (buy_price, total_buy_price, sell_price, total_sell_price)
    self.response.write(output)


application = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
