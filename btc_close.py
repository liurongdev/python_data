

import json
import pygal
from urllib.request import urlopen


json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"


response=urlopen(json_url)

content=response.read()

json_content=json.loads(content)
dates=[]
months=[]
weeks=[]
close=[]
weekdays=[]


for json_content_i in json_content:
    dates.append(json_content_i['date'])
    months.append(json_content_i['month'])
    weeks.append(json_content_i['week'])
    close.append(int(float(json_content_i['close'])))
    weekdays.append(json_content_i['weekday'])
    print(json_content_i)



line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title="收盘价"
line_chart.x_labels=dates

line_chart.add("收盘价",close)
N=20
line_chart.x_labels_major=dates[::N]
line_chart.render_to_file("收盘价折线图.svg")



