#!/usr/bin/python

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

class YFinanceFetcher:

  def __init__(self):
    None

  def getHist (self, symbol, startDate, endDate, info):
    query = yfinancequery.yfinancequery ()
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
      url = urllib2.urlopen (query.getHist(symbol, startDate, endDate, info));
      table = csv.DictReader (url.read().splitlines())
      return table

  def getStock (self, attr, symbols):
    query = yfinancequery.yfinancequery ()
    url = query.queryStock (attr, symbols)
    urldata = urllib2.urlopen (url)
    return list(csv.reader (urldata.read().splitlines()))

fetcher = YFinanceFetcher ()
f = fetcher.getHist ('BME.MC','1/01/2012', '1/12/2012', 'd+v')   # d, w, m, v, d+v
for row in f:
  print row

print fetcher.getStock ('GOOG,WU','a4d1nn4bcd')
