# coding:utf-8

import unittest
import time

class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case1的执行前置')


    def setUp(self):
        print('这个是case1的的前置条件')

    def tearDown(self):
        print('这个是case1的的后置条件')

    @unittest.skip('不执行第一条')
    def test_first01(self):
        print('test11')

    def test_first02(self):
        print('test12')
        # time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        print('所有case1的执行后置')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test_first02'))
    suite.addTest(FirstCase01('test_first01'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.TextTestRunner().run(suite)