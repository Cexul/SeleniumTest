#coding:utf-8
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from read_image import Read_image

class GetCode(object):
    def __init__(self,driver):
        self.driver = driver

    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element(By.ID, 'getcode_num')
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
        time.sleep(2)
        # print('-=-=-=-=-')

    # 解析图片验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        result = Read_image()
        # result = result.request(img_file=file_name)
        time.sleep(2)
        return result.request(img_file=file_name)