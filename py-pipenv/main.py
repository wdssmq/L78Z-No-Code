import json
import feedparser
import pprint

# 读取 rss
rss_list = feedparser.parse('https://www.wdssmq.com/feed.php')
# 提取标题和链接
rlt_list = [{'title': entry['title'], 'link':entry['link']} for entry in rss_list['entries']]
# 打印结果
pprint.pprint(rlt_list)
# 保存为 json 文件
with open('output.json', 'w') as f:
    json.dump(rlt_list, f)
