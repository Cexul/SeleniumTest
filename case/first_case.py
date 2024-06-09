# coding:utf-8
import os
import sys
sys.path.append('/Users/chenxuliang/PycharmProjects/selenium/')

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from log.user_log import UserLog



class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):

        options = webdriver.EdgeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=options)
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info('this is edge')


        self.login = RegisterBusiness(self.driver)
        self.file_name = '/Users/chenxuliang/Desktop/chen/图片/imooc1.png'

    def tearDown(self):
        # if sys.exc_info()[0]:
        #     self._outcome.errors
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + '/report/' +case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_log()


    def test_login_email_error(self):
        email_error = self.login.login_email_error('34', 'user1231', '111111', self.file_name)
        # print(email_error)
        self.assertFalse(email_error,'case执行，邮箱校验失败')
        # if email_error == True:
        #     print('case执行失败')

    def test_login_username_error(self):
        username_error = self.login.login_username_error('1235@163.com','25','111111',self.file_name)
        self.assertFalse(username_error,'case执行，用户名校验失败')

        # if username_error == True:
        #     print('case执行失败')

    def test_login_password_error(self):
        password_error = self.login.login_password_error('1235@163.com', '252341', '111', self.file_name)
        self.assertFalse(password_error,'case执行，密码校验失败')
        # if password_error == True:
        #     print('case执行失败')


    def test_login_code_error(self):
        code_error = self.login.login_code_error('1235@163.com', '252341', '111111', self.file_name)
        self.assertFalse(code_error,'case执行，验证码校验失败')
        # if code_error == True:
        #     print('case执行失败')

    def test_login_success(self):
        success = self.login.user_base('1235@163.com', '252341', '111111', self.file_name)
        self.assertFalse(success)
        # if self.login.register_success() == True:
        #     print('注册成功')

# def main():
#     first = FirstCase()
#     first.test_login_email_error()
#     first.test_login_username_error()
#     first.test_login_password_error()
#     first.test_login_code_error()
#     first.test_login_success()

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+'/report/'+'first_case.html')
    f = open(file_path,'wb')
    # with open(file_path,'wb') as f:
    #     f.write()
    # print(file_path)
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_success'))
    # unittest.TextTestRunner().run(suite)

    runner = HTMLTestRunner.HTMLTestRunner(stream = f,title='this is first report',description='第一次测试报告',verbosity=2)
    runner.run(suite)
    # runner.run()

