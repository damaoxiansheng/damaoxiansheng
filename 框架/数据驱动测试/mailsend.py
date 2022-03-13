import smtplib#发送邮件
import os
#封装邮件内容
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 发送邮件的类
class mailsend():
    def sendFujian(self,filename):
        #设置发送邮箱服务器：smtp.163.com
        smtpserver = "smtp.163.com"
        #设置邮箱的用户名及密码,用于邮箱登录：xiaowang@163.com
        username = "a371150995@163.com"
        #大家自己的qq邮箱、163邮箱的授权码
        # 不是登录密码
        password = "CUGIYCANHYFKQIVB"
        #设置发送邮箱，就是你的登录邮箱
        sender = "a371150995@163.com"
        #设置接收邮箱
        receiver = "371150995@qq.com"
        # receiver = "xxx@qq.com"
        #设置邮箱主题
        subject = "电商自动化测试结果"

        # 下面的是后续可能要修改的代码，从当前文件找到html报告文件的位置
        # path2 = os.path.dirname(os.path.dirname(__file__))+r"/test_reports/"
        # path = path2+filename+".html"
        path = os.path.dirname(__file__)+r"/"+filename+r".html"

        # 读取html文件
        content = open(path,"rb").read()

        # 下面的代码不用改
        msg = MIMEText(content,"base64","utf-8")
        msg["Content-Type"]="application/octet-stream"
        msg['Content-Disposition'] = "attachment;filename='%s.html'" %filename

        msgRoot = MIMEMultipart('related')
        msgRoot["Subject"]=subject
        msgRoot["From"] = sender
        msgRoot["To"]= receiver
        msgRoot.attach(msg)

        #创建一个邮件发送服务的对象
        smtp = smtplib.SMTP()
        #连接发件服务器
        smtp.connect(smtpserver)
        #登录发件邮箱
        smtp.login(username,password)
        #发送邮件
        smtp.sendmail(sender,receiver,msgRoot.as_string())
        smtp.quit()

if __name__=="__main__":
    ssend = mailsend()
    ssend.sendFujian(r"2021-12-06-14-43")