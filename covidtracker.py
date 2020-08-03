#Enter 2 letter Country Code as input
#Output Date Format MM/DD/YY
from urllib.request import Request,urlopen
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
cc=input('Country Code: ')
api='https://thevirustracker.com/free-api?countryTimeline='
url=api+cc
req=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
uh=urlopen(req,context=ctx).read()
data=json.loads(uh)
ndc,max,mdate=0,0,str()
for x in data['timelineitems'][0]:
    if x == 'stat':
        continue
    ndc=int(data['timelineitems'][0][x]['new_daily_cases'])
    if max<ndc:
        max=ndc
        mdate=x
print('MAXIMUM DAILY NEW CASES ON',mdate,'WITH A COUNT OF',str(max),'IN',data['countrytimelinedata'][0]['info']['title'])