"""
    百度翻译案例： ---get
        需要的参数：
            请求的url地址：
            请求的method方法：get

"""
import requests

# 定义请求参数
url = "https://fanyi-api.baidu.com/api/trans/vip/translate?q=apple&from=auto&to=zh&appid=20211223001036268&salt=888888&sign=5fd25cf030973dea81fbbdd268f324e0"

# 使用requests中的get方法来实现
# =的左侧:响应报文对象,包括响应状态行、响应头部和响应正文
# =的右侧:打包请求,并发送请求,并返回Response对象。
response = requests.get(url)

# 查看响应正文
# text是将正文转化为字符串显示
# print(response.text)
# json是将正文转为python中的字典和列表形式(前提响应的正文必须是json结构的)
print(response.json())
print(response.json()["trans_result"][0]["dst"])
print(str(response.json()))
if "苹果" in str(response.json()):
    print("测试通过")
