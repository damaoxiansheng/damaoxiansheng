import re

import requests

session = requests.session()

a1 = session.get(url="http://localhost:81/verydows-master/index.php?m=backend&c=main&a=index")
a = a1.text
c = re.findall('name="(.*?)" value="(.*?)"', a)
c1 = c[0][0]
c2 = c[0][1]

a2 = session.post(url="http://localhost:81/verydows-master/index.php?m=backend&c=main&a=login",
                  headers={
                      "Content-Type": "application/x-www-form-urlencoded"},
                  data={
                      c1: c2,
                      "username": "admin",
                      "password": "200c6d94e583e62c6964de3acdc723e5"
                  })

a3 = session.post(url="http://localhost:81/verydows-master/index.php?m=backend&c=goods&a=add&step=submit",
                  data={
                    "goods_name": "顶呱呱纸尿裤2",
                    "cate_id": "0",
                    "brand_id": "0",
                    "goods_sn": "0002",
                    "now_price": "100",
                    "original_price": "200",
                    "newarrival": "1",
                    "status": "1",
                    "goods_image": "",
                    "stock_qty": "9999",
                    "goods_weight": "0.00",
                    "meta_keywords": "",
                    "meta_description": "",
                    "goods_brief": "<p>这是非常好用的纸尿裤！</p>"
                  })
print(a3.content.decode("utf-8"))
