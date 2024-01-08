from urllib.request import urlopen

URL = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9332224727344160901%22%7D&n_type=-1&p_from=-1'

response = urlopen(URL)

data = response.read()

with open('webcrawler/store.html', 'wb') as write_html:
    write_html.write(data)

# 等同于
# str = data.decode('utf-8')
# with open('webcrawler/store.html', 'w') as write_html:
#     write_html.write(str)



