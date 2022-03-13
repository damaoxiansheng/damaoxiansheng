from guanjianzi_qudong import guanjianzi_qudong

driver = guanjianzi_qudong("Chrome")
driver.wangzhi("https://www.baidu.com/")
driver.yuansu("id", "kw")
driver.shuru("id", "kw", "中国人")
driver.dianji("id", "su")
driver.dengdai(5)
driver.tuichu()