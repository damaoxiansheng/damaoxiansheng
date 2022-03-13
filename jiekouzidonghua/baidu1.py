import requests
response = requests.get("https://www.baidu.com/")
print(response)
# 查看状态码的值
print(response.status_code)
# 查看响应头部字段
print(response.headers["Content-type"])
# 查看响应正文的编码
print(response.encoding)
# 查看响应正文
print(response.text)
# 响应正文，以字节码形式显示
print(response.content.decode("utf-8"))
# 响应报文中保存请求的url地址
print(response.url)
# 响应报文中的cookie字段
print(response.cookies)