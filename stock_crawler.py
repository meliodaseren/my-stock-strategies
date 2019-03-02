#!/usr/bin/env pyhon

import requests
from bs4 import BeautifulSoup

r = requests.get("https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=0056")

