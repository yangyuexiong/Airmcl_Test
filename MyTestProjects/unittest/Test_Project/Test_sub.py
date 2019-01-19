from Test_class_1 import *
from Test_StartEnd import *

#@unittest.skip('跳过测试')
#@unittest.skipIf(2>1,'判断条件跳过测试')
#@unittest.skipUnless(1 > 2, '条件为假-跳过测试')
#@unittest.expectedFailure#预期失败跳过测试
class TestSub(Test_StarEnd):
    # 运行前执行
    @classmethod
    def setUpClass(cls):
        print('开始测试>>>>>>>>>>>>>>>>>>')
    @classmethod
    def tearDownClass(cls):
        print('结束测试>>>>>>>>>>>>>>>>>>')

    def test_sub(self):
        i=Math(3,1)
        self.assertEqual(i.sub(),2)