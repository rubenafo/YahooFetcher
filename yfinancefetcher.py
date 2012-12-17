# Copyright 2012 Ruben Afonso, http://www.figurebelow.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import csv;
import urllib2;
import yfinancequery;

#
# This class invokes a query builder, fetches the content from the received URL
# and returns the result
#

class YFinanceFetcher:

  def __init__(self):
    None

  # Gets historical data.
  # - symbol: an list of stock symbols, e.g. 'GOOG,MICRO'
  # - starDate: starting date, e.g 12/5/2012 for 12th of May of 2012
  # - endDate: end date
  # - info: interval time. Accepted values:
  #   d daily, w weekly, m monthly, v dividends, and d+v for daily data and dividends
  #
  def getHist (self, symbol, startDate, endDate, info):
    query = yfinancequery.YFinanceQuery ()
    if (info == "d+v"):
      url_daily = urllib2.urlopen (query.getHist(symbol, startDate, endDate, "d"))
      table_daily = csv.reader (url_daily.read().splitlines())
      url_div = urllib2.urlopen (query.getHist(symbol, startDate, endDate, "v"))
      table_div = csv.reader (url_div.read().splitlines())
      table_daily = list(table_daily)
      table_div = list(table_div)
      if (len(table_div) > 0):
        for rowdaily in table_daily:
          hasdiv = False
          for rowdiv in table_div:
            # matching dates? This also matches the headers, adding
            # automagically the 'Dividends' column ...
            if (rowdaily[0] == rowdiv[0]):
              rowdaily.append(rowdiv[1])
              hasdiv = True
              break
          if (hasdiv == False):
            rowdaily.append (0)
      return table_daily
    else:
      if (info in ['w','m','d']):
        url = urllib2.urlopen (query.getHist(symbol, startDate, endDate, info));
        table = csv.reader (url.read().splitlines())
        return table
      else:
        print "Error: invalid time option in getHist(): " + info
        return []

  # Gets current stock data.
  # - attr: list of stock symbols e.g. 'GOOG,MICRO'
  # - symbols:
  def getStock (self, attr, symbols):
    query = yfinancequery.YFinanceQuery ()
    url = query.queryStock (attr, symbols)
    urldata = urllib2.urlopen (url)
    return list(csv.reader (urldata.read().splitlines()))

