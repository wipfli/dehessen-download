import requests
import json
from urllib.parse import quote

r = requests.get('https://gds.hessen.de/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten/Digitales%20Gel%C3%A4ndemodell%20(DGM1)&navigation=all')

nav = json.loads(r.text)

urls = []
for item in nav['navigation']:
    if not item['uri'].startswith('/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2F'):
        continue
    quoted_name = quote(item['name'])
    url = f'https://gds.hessen.de/downloadcenter/20260824/3D-Daten/Digitales%20Gel%C3%A4ndemodell%20(DGM1)/{quoted_name}/PKT_{quoted_name}.zip'
    urls.append(url)

with open('file_list.txt', 'w') as f:
    f.write('\n'.join(urls))
