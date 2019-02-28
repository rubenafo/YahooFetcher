#
# Copyright 2019, Ruben Afonso - http://www.github.com/rubenafo
# Licensed under the Apache License (see the LICENSE file)
#
from QueryBuilder import Query
import ComponentsExtractor

#
# This class invokes a query builder, fetches the content from the received URL
# and returns the result
#

class YahooFetcher:

  def __init__(self):
    self.query = Query()

  #
  # Gets historical data in json format.
  #
  # Output: ticker, date, open, high, low, close, volume, adjusted close
  #
  def getHistAsJson (self, symbol, startDate, endDate, event="quote", verbose=False):
    rows = self.query.getHistURL(symbol, startDate, endDate, event, verbose)
    fullData = [data.split(",") for data in rows]
    jsonList = [];
    if event == "quote":
      for elem in fullData:
        json = {'date': elem[0],
                'o': float(elem[1]) if elem[1] != 'null' else 0,
                'h': float(elem[2]) if elem[2] != 'null' else 0,
                'l': float(elem[3]) if elem[3] != 'null' else 0,
                'c': float(elem[4]) if elem[4] != 'null' else 0,
                'adjc': float(elem[5]) if elem[5] != 'null' else 0,
                'v': int(elem[6]) if elem[6] != 'null' else 0,
                "ticker":symbol};
        jsonList.append(json)
      return jsonList
    elif event == "div" or event == "split":
      for elem in fullData[1:]:
        json = {"date":elem[0], event:float(elem[1])}
        jsonList.append(json)
      return jsonList

  def getComponents(self, index):
    return ComponentsExtractor().getComponents(index);

