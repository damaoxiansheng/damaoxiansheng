import json

import requests

with open(r"D:\pythonzuoye\jiekouzidonghua\shuju.json", "r", encoding="utf-8") as f:
    a = json.load(f)
    for i in a:
        a = requests.post(url="http://39.101.167.251/qftest/index.php",
                          data={"username": i['username'],
                                "email": i['email'],
                                "password": i['password'],
                                "repassword": i['repassword'],
                                "agree": i['agree']},
                          params={"c": "user",
                                  "a": "register",
                                  "step": "submit"},
                          headers={"Content-Type": "application/x-www-form-urlencoded"})

        if "恭喜您，注册成功！" in a.content.decode("utf-8"):
            print("用例执行成功！")
        else:
            print("用例执行失败！")
