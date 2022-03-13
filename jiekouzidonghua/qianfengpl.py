import requests
url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=302090&count=10&page=0&filter_rating=0&bkn=926800621&r=0.037183389811309864"
headers = {
    "referer": "https://ke.qq.com/course/302090?taid=2237639306812426"
}
response = requests.get(url = url,headers=headers)

yq = "1527770112"
sj = str(response.json()["result"]["items"][0]["first_comment_time"])
if yq == sj :
    print("pass")