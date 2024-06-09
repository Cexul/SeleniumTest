# coding:utf-8


from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement
from read_image import Read_image

class ActionMethod(object):

    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self,browser):
        options = webdriver.EdgeOptions()
        options.add_experimental_option('detach', True)
        if browser =='Edge':
            self.driver = webdriver.Edge(options=options)
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = webdriver.Firefox(options=options)

    # 输入地址
    def get_url(self,url):
        self.driver.get(url)


    # 定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self,key):
        self.get_element(key).click()

    # 等待
    def sleep_time(self):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title
