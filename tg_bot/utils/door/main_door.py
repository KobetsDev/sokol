import requests
import time

bltk = 'MlFHbHQxs-QRIP5HHPPedEUsDTDCEw6E'


# room = float(requests.get('http://blynk-cloud.com/'+bltk+'/get/V1').json()[0])
# requests.get('http://blynk-cloud.com/'+bltk+'/get/V5').content == b'["1"]'
# requests.get('http://blynk-cloud.com/'+bltk+'/update/V5?value=0')

def opendoor():
    requests.get('http://blynk-cloud.com/'+bltk+'/update/V0?value=1')
    time.sleep(1)
    return requests.get('http://blynk-cloud.com/'+bltk+'/get/V0').content == b'["1"]'

