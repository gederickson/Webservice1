import suds
import sys
import lxml.etree as etree

def xml_pretty_print(doc):
    return etree.tostring(doc, pretty_print = True)

url = "http://www.webservicex.net/stockquote.asmx?wsdl"

# get ticker symbol as command line arg or use default
ticker_symbol = len(sys.argv) > 1 and sys.argv[1] or 'TLK'

print 'opening WSDL: %s...' % url,
client = suds.client.Client(url)
print 'Ok'

print 'Sending request...',
xml_response = client.service.GetQuote(ticker_symbol)
print 'Ok'

doc = etree.fromstring(xml_response)

# print formatted XML response
# print xml_pretty_print(doc)
stock = doc[0] #get first node

for elem in stock:
    print '%s: %s' % (elem.tag.rjust(16), elem.text)