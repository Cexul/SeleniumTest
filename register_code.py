#coding:utf-8
import random
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Edge(options=options)

# 浏览器初始化
def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(2)

# 获取element信息
def get_element(id):
    element = driver.find_element(By.ID,id)
    return element

# 获取随机数
def get_range_user():

    user_info = ''.join(random.sample('1234567890asdcfvgqertyuiplmnbvcxz', 8))
    return user_info

def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element(By.ID, 'getcode_num')
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    # print(left, top, right, height)
    # img = im.crop((left,top,right,height))

    img = im.crop((1237, 1056, 1486, 1133))
    img.save(file_name)

# 解析图片验证码
def code_online():
    return 1234

def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+'@163.com'
    file_name = '/Users/chenxuliang/Desktop/chen/图片/imooc1.png'
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element('register_password').send_keys('123456')
    get_code_image(file_name)
    text = code_online()
    get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()
    # driver.close()

run_main()
