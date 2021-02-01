import pandas as pd
import time
import datetime
import requests
from urllib.request import Request, urlopen
import lineTool
import linepush
import csv
from opencc import OpenCC
#定義並取得今天和昨天strftime後的日期
td=time.strftime("%Y%m%d")
def Yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today-oneday
    return yesterday
YT = Yesterday()
yd = datetime.date.strftime(YT, '%Y%m%d')

Date=time.strftime("%Y%m%d")
url='https://rl.fx678.com/date/' + Date + '.html'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
page = urlopen(req)
fx = pd.read_html(page)

fxx = fx[0]
fxx.to_csv('forexnews' + Date + '.csv')




df = pd.read_csv('forexnews' + Date + '.csv')
print(df)
