import requests

a = requests.get(
    url="https://www.kuaidi100.com/query?type=yuantong&postid=YT6074326614455&temp=0.9967225855011113&phone=")

if "ok" in a.text:
    print("测试通过！")
