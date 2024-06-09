# coding:utf-8

# 数据驱动，邮箱用户名密码验证码，错误信息定位元素，错误提示信息

import ddt
import unittest
import os
import sys
import unittest

from business.register_business import RegisterBusiness
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from util.excel_util import ExcelUtil


ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=options)
        self.driver.get('http://www.5itest.cn/register')

        self.login = RegisterBusiness(self.driver)
        self.file_name = '/Users/chenxuliang/Desktop/chen/图片/imooc1.png'

    def tearDown(self):
        # if sys.exc_info()[0]:
        #     self._outcome.errors
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + '/report/' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()


    '''
    @ddt.data(
        ['12', 'chens', '123456', '/Users/chenxuliang/Desktop/chen/图片/imooc1.png', 'user_email_error', '请输入有效的电子邮件地址'],
        ['1235@163.com','25','111111','/Users/chenxuliang/Desktop/chen/图片/imooc1.png','user_email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack
    '''

    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        print(email_error)
        self.assertFalse(email_error,'case执行，邮箱校验失败')
        # if email_error == True:
        #     print('case执行失败')


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+'/report/'+'first_case2.html')
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is first report2', description='第er次测试报告',
                                           verbosity=2)
    runner.run(suite)
