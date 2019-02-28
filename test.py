#!/usr/bin/python

#
# Copyright 2017, Ruben Afonso - http://www.github.com/rubenafo
# Licensed under the Apache License (see the LICENSE file)
#

import YahooFetcher
import ComponentsExtractor

c = ComponentsExtractor.ComponentsExtractor(verbose=True)
#ex = c.getExchange("mse")
ex = c.getComponents("nasdaq")
for e in ex:
  print e
