import suds
import xml.etree.ElementTree as etree

url = 'http://www.webservicex.net/globalweather.asmx?WSDL'

print 'Membuka WSDL: %s...' % url
client = suds.client.Client(url)
print 'OK'

city = 'Jakarta'
country = 'Indonesia'

print 'Mengirim request cuaca untuk Kota %s Negara %s...' % (city, country)
xml = client.service.GetWeather(city, country)
print 'OK'


xml = xml.encode('utf16')


parse = etree.fromstring(xml)

print '                             JAKARTA HARI INI'
print '-------------------------------------------------------------------------------'
print parse.find('Location').text
print 'Per ', parse.find('Time').text
print '-------------------------------------------------------------------------------'
print 'Angin'.ljust(18), ': ', parse.find('Wind').text
print 'Jarak Penglihatan'.ljust(18), ': ', parse.find('Visibility').text
print 'Cuaca'.ljust(18), ': ', parse.find('SkyConditions').text
print 'Suhu'.ljust(18), ': ', parse.find('Temperature').text
print 'Titik Embun'.ljust(18), ': ', parse.find('DewPoint').text
print 'Kelembapan'.ljust(18), ': ', parse.find('RelativeHumidity').text
print 'Tekanan'.ljust(18), ': ', parse.find('Pressure').text

print 'OK'