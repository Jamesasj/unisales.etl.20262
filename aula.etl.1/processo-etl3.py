from urllib.request import urlopen
## WebScraping

url = "https://www.uol.com.br/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print('Menezes' in html)