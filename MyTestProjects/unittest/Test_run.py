import unittest

test_dir = './'
print(test_dir)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')

if __name__ == '__main__':
    # unittest.main()
    # 构造测试集/多个用例整合
    # suite = unittest.TestSuite()

    # 增加用例  类+方法"test_add" 按添加顺序执行
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add1"))
    # suite.addTest(TestAdd("assertTrue_text"))
    # suite.addTest(TestAdd("assertIn_test"))
    # suite.addTest(TestAdd("assertIs_test"))
    #
    # suite.addTest(TestSub("test_sub"))

    # 执行测试
    runer = unittest.TextTestRunner()
    runer.run(discover)
