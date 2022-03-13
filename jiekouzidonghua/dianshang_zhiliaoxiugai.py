import requests

a = requests.post(url="http://39.101.167.251/qftest/user/profile.html",
                  params={"step": "update"},
                  headers={
                      "Cookie": "VDSSKEY=qq85pnklauo4g6ft8sv3vovtm4; PHPSESSID=om2ce3np7c0r4ao9upit2uato5; deviceid=1640588428402; xinhu_mo_adminid=oa0stt0sza0ssa0ar0gz0szj0gs0oa0ax0szj0ga02; xinhu_ca_adminuser=admin; xinhu_ca_rempass=0; LOGINED_USER=sdgdsfsa; USER_AVATAR=2112%2F3a9cd89550743ea4442cc4a7b0eeb0a5.png",
                      "Content-Type": "application/x-www-form-urlencoded"},
                  data={"nickname": "张云辉",
                        "qq": "199839022",
                        "gender": "1",
                        "birth_year": "1998",
                        "birth_month": "10",
                        "birth_day": "21",
                        "signature": "爷！狂傲霸天！"})

print(a.content.decode("utf-8"))