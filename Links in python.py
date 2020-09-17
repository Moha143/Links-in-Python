import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fatama.html'
position = int(input("Enter position:")) - 1
count = int(input("Enter count:"))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
name_list = []
link_tags = soup('a')

for i in range(count):
    link = link_tags[position].get('href', None)
    print("Retrieving:", link)
    name_list.append(link_tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    link_tags = soup('a')
    link = link_tags[position].get('href', None)

print(name_list[-1])
