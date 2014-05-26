import suds
import lxml.etree as etree
client = suds.client.Client("http://www.webservicex.net/stockquote.asmx?wsdl")
doc = etree.fromstring(client.service.GetQuote('TLK'))
stock = doc[0]
for elem in stock:
    print '%s: %s' % (elem.tag.rjust(16), elem.text)
