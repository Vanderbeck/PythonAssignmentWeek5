#Assignment 1
import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL:')
data = urllib.urlopen(url).read() #'http://python-data.dr-chuck.net/comments_42.xml').read()

tree = ET.fromstring(data)

tree_lst = tree.findall('comments/comment')

total = 0.0
for item in tree_lst:
    txt = item.find('count').text
    num = float(txt)
    total = total + num

print total
