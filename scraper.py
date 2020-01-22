# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import scraperwiki
from urllib2 import urlopen
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile
import csv
# from collections import OrderedDict
import json


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

url = "https://avaandmed.rik.ee/andmed/ARIREGISTER/ariregister_csv.zip"
response = urlopen(url)
print("Gotten response.")
with ZipFile(BytesIO(response.read())) as zfile:
    print("Pulled zip file.")
    with zfile.open(ZipFile.namelist(zfile)[0], 'r') as csvfile:
        print("Opened zip file.")
        with TextIOWrapper(csvfile, encoding="utf-8-sig") as text:
            reader = list(csv.reader(utf_8_encoder(text), delimiter=str(";")))
print("Done reading CSV")
head = reader[0]
print(head)
data = reader[1:]
table = []
for i in data:
    reader = dict(zip(head, i))
    table.append(reader)
scraperwiki.sqlite.save(['ariregistri_kood'], data=table, table_name='ee-companies')
# scraperwiki.sqlite.save(unique_keys=['name'], data=[{"name": "susan", "occupation": "software developer"},{"name": "david", "occupation": "developer"}])  
