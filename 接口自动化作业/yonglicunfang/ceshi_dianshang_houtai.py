import os
import sys
import unittest
import json
import requests
import re

path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname("__file__"))))
sys.path.append(path)

from gonggong import rizhi

session = requests.session()

class dianshang_houtai(unittest.TestCase):

    def setUp(self):
        a1 = session.get(url="http://192.168.31.247:81/verydows-master/index.php?m=backend&c=main&a=index")
        self.zz = re.findall('name="(.*?)" value="(.*?)"', a1.content.decode("utf-8"))[0]
        print(self.zz[0])
        print(self.zz[1])

    def test01_houtai_denglu(self):
        """电商后台登陆"""
        a1 = session.post(url="http://192.168.31.247:81/verydows-master/index.php?m=backend&c=main&a=login",
                          headers={"Content-Type": "application/x-www-form-urlencoded"},
                          data={self.zz[0]: self.zz[1],
                                "username": "admin",
                                "password": "200c6d94e583e62c6964de3acdc723e5"})
        self.assertIn("refresh", a1.content.decode("utf-8"))
        rizhi.rizhi("电商后台登陆用例  预期=refresh  实际=%s" % (a1.content.decode("utf-8")))

    def test02_add_shangping(self):
        """添加商品"""
        a1 = session.post(url="http://192.168.31.247:81/verydows-master/index.php?m=backend&c=goods&a=add&step=submit",
                          data={"goods_name": "顶呱呱无敌纸尿裤",
                                "cate_id": "0",
                                "brand_id": "0",
                                "goods_sn": "0003",
                                "now_price": "100",
                                "original_price": "200",
                                "newarrival": "1",
                                "status": "1",
                                "goods_image": "",
                                "stock_qty": "9999",
                                "goods_weight": "0.00",
                                "meta_keywords": "",
                                "meta_description": "",
                                "goods_brief": '<p><span style="white-space: normal;">顶呱呱无敌纸尿裤</span></p><br/><p><br/></p>'}
                          )
        self.assertIn("添加商品成功", a1.content.decode("utf-8"))
        rizhi.rizhi("电商后台添加商品登陆用例  预期=添加商品成功  实际=%s" % (a1.content.decode("utf-8")))

    def test03_add_fenlei(self):
        """添加分类"""
        a1 = session.post(url="http://192.168.31.247:81/verydows-master/index.php?m=backend&c=goods_cate&a=add&step=submit",
                          data={"cate_name": "铁锤类6",
                                "parent_id": "0",
                                "meta_keywords": "大铁锤妹妹",
                                "meta_description": "这是一个大铁锤",
                                "seq": "1"}
                          )
        self.assertIn("添加商品分类成功", a1.content.decode("utf-8"))
        rizhi.rizhi("电商后台添加商品分类用例  预期=添加商品分类成功  实际=%s" % (a1.content.decode("utf-8")))

    def test04_add_xuanxiang(self):
        """新增选项类型"""
        a1 = session.post(url="http://192.168.31.247:81/verydows-master/index.php?m=backend&c=goods_optional_type&a=add&step=submit",
                          data={"name": "无敌铁锤6"})
        self.assertIn("添加选项类型成功", a1.content.decode("utf-8"))
        rizhi.rizhi("电商后台添加添加选项类型用例  预期=添加选项类型成功  实际=%s" % (a1.content.decode("utf-8")))

    def test05_add_yonghuzu(self):
        """添加新用户组用例"""
        a1 = session.post(url="http://192.168.31.247:81/verydows-master/index.php?m=backend&c=user_group&a=add&step=submit",
                          data={"group_name": "无敌组6",
                                "min_exp": "14",
                                "discount_rate": "100"}
                          )
        self.assertIn("添加用户组成功", a1.content.decode("utf-8"))
        rizhi.rizhi("电商后台添加用户组用例  预期=添加用户组成功  实际=%s" % (a1.content.decode("utf-8")))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
