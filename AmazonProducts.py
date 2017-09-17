#! /usr/bin/python3

import requests,sys,webbrowser,bs4

print('Fetching products...')
res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords='+' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.s-item-container a.a-link-normal, a.s-access-detail-page ,a.s-color-twister-title-link,a.a-text-normal')
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))

