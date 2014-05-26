'''
Created on 24 Mei 2014

@author: angga
'''
from suds.client import Client

url = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'

client = Client(url)
currency = client.service.ConversionRate('USD','IDR')
print currency