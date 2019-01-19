from Test_class_1 import *
from Test_StartEnd import *


class TestAdd(Test_StarEnd):

    #自定义测试方法
    def test_add(self):
        j=Math(5,10)
        #断言
        #是否等于
        self.assertEqual(j.add(),15)
        #self.assertEqual(j.add(),12)

    def test_add1(self):
        j = Math(5, 10)
        #是否不等于
        self.assertNotEqual(j.add(),12)

    def assertTrue_text(self):
        j = Math(5, 10)
        #是否为真
        self.assertTrue(j.add()>10)

    def assertIn_test(self):
        #a是否在b里面
        self.assertIn('1','1,2')

    def assertIs_test(self):
        #a是否与b一样
        self.assertIs('yyx','yyx')