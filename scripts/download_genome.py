#!../venv/bin/python
import requests
from html.parser import HTMLParser


class NcbiFtpHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


url = "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/"
r = requests.get(url)
print(r.status_code)
print(r.headers["content-type"])
print(r.text)

parser = NcbiFtpHTMLParser()
print(parser.feed(r.text))
