import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url="http://api.github.com/search/repositories?q=language:python&sort=starts"

r=requests.get(url)

print("status_code",r.status_code)

json_data=r.json()

#获取仓库信息
repo_dict=json_data["items"]

names,starts=[],[]

for item in repo_dict:
    names.append(item["name"])
    starts.append(item["stargazers_count"])


my_style=LS("#333366",base_style=LCS)

chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title="Title"

chart.x_labels=names

chart.add("星星数量",starts)

chart.render_to_file("python_repo.svg")



print(json_data)
