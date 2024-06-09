#coding:utf-8

from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement
from read_image import Read_image

class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    # 浏览器初始化，获取浏览器驱动对象driver
    def get_driver(self,url,i):
        if i == 1:
            options = webdriver.EdgeOptions()
            options.add_experimental_option('detach', True)
            driver = webdriver.Edge(options=options)
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            driver = webdriver.Chrome(options=options)
        driver.get(url)
        # driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self,key,data):

        user_element = self.get_user_element(key)
        user_element.send_keys(data)


    # 定位用户信息，获取元素element，用户名，密码，邮箱
    def get_user_element(self,key):
        """
        定位用户信息，获取元素element，用户名，密码，邮箱
        :param key: 配置文件中的user_email等
        :return: 返回元素信息
        """
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_user(self):

        user_info = ''.join(random.sample('1234567890asdcfvgqertyuiplmnbvcxz', 8))
        return user_info

    def get_code_image(self,file_name):


        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('code_image')
        # print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        # print(left, top, right, height)
        # img = im.crop((left,top,right,height))

        img = im.crop((1237, 1056, 1486, 1133))
        img.save(file_name)
        # print('-=-=-=-=-')

    # 解析图片验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        result = Read_image()
        # result = result.request(img_file=file_name)
        return result.request(img_file=file_name)


    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + '@163.com'
        file_name = '/Users/chenxuliang/Desktop/chen/图片/imooc1.png'
        code_text = self.code_online(file_name)
        # print('code_text',code_text)
        # print(user_email)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password', '111111')
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print('注册成功')
        else:
            print('注册失败')
            self.driver.save_screenshot('/Users/chenxuliang/Desktop/chen/图片/codeerror.png')
        time.sleep(1)
        self.driver.close()

if __name__ == '__main__':
    for i in range(2):

        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()