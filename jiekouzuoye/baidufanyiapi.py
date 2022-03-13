import hashlib
import requests

def xianshi():
    return print("==============百度翻译api================""\n"
                 "         1:翻译           2:退出""\n"
                 "========================================")

def tuichu():
    return print("===============欢迎再次使用===============")

def fanyi():
    return print("============您现在可以进行翻译了===========""\n"
                 "可选的输入语言形式：1-自动   2-英文   3-中文")

def jieguo():
    return print("===============翻译结果是===============")

def getStrAsMD5(parmStr):
    if isinstance(parmStr, str):
        parmStr = parmStr.encode("utf-8")
        m = hashlib.md5()
        m.update(parmStr)
        return m.hexdigest()

def gongneng(a, q):
    b = {"1": "auto", "2": "en", "3": "zh"}[a]
    o = {"1": "zh", "2": "en", "3": "jp", "4": "kor"}[q]
    shuru = input("请输入要翻译的文字：")
    print("===============翻译结果是===============")
    md5zhi = ("20211223001036267" + shuru + "aaa" + "M8PcpMGHWMFagK15I3M0")
    jieguo = requests.get(url="https://fanyi-api.baidu.com/api/trans/vip/translate",
                          params={"q": shuru,
                                  "from": b,
                                  "to": o,
                                  "appid": "20211223001036267",
                                  "salt": "aaa",
                                  "sign": getStrAsMD5(md5zhi)})
    print("您输入的是：" + shuru)
    print("翻译结果是：" + jieguo.json()["trans_result"][0]["dst"])

while True:
    xianshi()
    zhi = int(input("请选择要执行的功能："))
    if zhi == 2:
        tuichu()
        break
    elif zhi == 1:
        fanyi()
        zhi2 = input("请选择输入语言形式：")
        print("可选的翻译语言形式:1-中文 2-英文 3-日文 4-韩文")
        zhi3 = input("请选择输入语言形式：")
        gongneng(zhi2, zhi3)
    else:
        print("请输入正确选项！")