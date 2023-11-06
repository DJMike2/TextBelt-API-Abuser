import requests
import urllib3

urllib3.disable_warnings()


proxies = {"http": "http://185.180.231.30:443", "https": "http://185.180.231.30:443"}
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'}

resp = requests.post('https://textbelt.com/text', {
  'phone': 'PHONE NUMBER',
  'message': 'BLA BLA BLA',
  'key': 'textbelt'
},verify=False, headers=headers, proxies=proxies)


print(resp.json())
