import xml.etree.ElementTree as etree
from suds.client import Client
url = 'http://www.webservicex.net/stockquote.asmx?wsdl'
client = Client(url)
xml = client.service.GetQuote ('TLK')

xml = xml.encode('utf16')

parse = etree.fromstring(xml)

print 'Symbol'.ljust(18), ': ', parse.find('Stock/Symbol').text
print 'Last'.ljust(18), ': ', parse.find('Stock/Last').text
print 'Date'.ljust(18), ': ', parse.find('Stock/Date').text
print 'Time'.ljust(18), ': ', parse.find('Stock/Time').text
print 'Change'.ljust(18), ': ', parse.find('Stock/Change').text
print 'Open'.ljust(18), ': ', parse.find('Stock/Open').text
print 'High'.ljust(18), ': ', parse.find('Stock/High').text
print 'Low'.ljust(18), ': ', parse.find('Stock/Low').text
print 'Volume'.ljust(18), ': ', parse.find('Stock/Volume').text
print 'MktCap'.ljust(18), ': ', parse.find('Stock/MktCap').text
print 'PreviousClose'.ljust(18), ': ', parse.find('Stock/PreviousClose').text
print 'PercentageChange'.ljust(18), ': ', parse.find('Stock/PercentageChange').text
print 'AnnRange'.ljust(18), ': ', parse.find('Stock/AnnRange').text
print 'Earns'.ljust(18), ': ', parse.find('Stock/Earns').text
print 'P-E'.ljust(18), ': ', parse.find('Stock/P-E').text
print 'Name'.ljust(18), ': ', parse.find('Stock/Name').text
