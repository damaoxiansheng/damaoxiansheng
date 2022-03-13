# 需求：使用request方法来实现get请求
# 导包
import requests

# 对于百度的首页接口，只需要打包url和method两个参数即可
url = "https://www.baidu.com/"
method = "get"

# 发送请求
# 关键字传参
response = requests.request(method=method, url=url)
# 位置传参
# response = requests.request(method, url)

# 查看响应正文
print(response.content.decode("utf-8"))
