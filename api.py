import requests
import json
import pandas
import matplotlib.pyplot as plt
r = requests.get('https://quality.data.gov.tw/dq_download_json.php?nid=9337&md5_url=d60725c702426095eba13e0ca21a768c')
r.encoding = 'utf-8'
data = json.loads(r.text)

boy = []
boy2 = []
for i in data:
    boy.append(float(i['男性 (%)']))
    boy2.append(i['年份別'])


plt.plot(boy2,boy)
plt.ylabel('man(%)')
plt.xlabel('yaer')
plt.show()


girl = []
girl2 = []
for i in data:
    girl.append(float(i['女性 (%)']))
    girl2.append(i['年份別'])

plt.plot(girl2,girl)
plt.ylabel('girl(%)')
plt.xlabel('yaer')
plt.show()

tatol = []
tatol2 = []
for i in data:
    tatol.append(float(i['合計 (%)']))
    tatol2.append(i['年份別'])

plt.plot(tatol2,tatol)
plt.ylabel('total(%)')
plt.xlabel('yaer')
plt.show()


