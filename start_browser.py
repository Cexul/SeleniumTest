#coding=utf-8
import random
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image




options = webdriver.EdgeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Edge(options=options)


# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=options)
driver.get('http://www.5itest.cn/register')
# driver.maximize_window()
# time.sleep(1)
# print(EC.title_contains('注册'))
email_element = driver.find_element(By.ID,'register_email')
for i in range(5):

    user_email = ''.join(random.sample('1234567890asdcfvg',5))+'@163.com'

# element = driver.find_element(By.CLASS_NAME,'controls')
# locator = (By.CLASS_NAME,'controls')
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
# # driver.close()
#
# print(email_element.get_attribute('placeholder'))
email_element.send_keys(user_email)
print(email_element.get_attribute('value'))
#
driver.save_screenshot('/Users/chenxuliang/Desktop/chen/图片/imooc.png')
code_element = driver.find_element(By.ID,'getcode_num')
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open('/Users/chenxuliang/Desktop/chen/图片/imooc.png')
print(left,top,right,height)
# img = im.crop((left,top,right,height))

img = im.crop((1237,1056,1486,1133))
img.save('/Users/chenxuliang/Desktop/chen/图片/imooc1.png')

# out = img.resize((2304,3218))
# out.save('/Users/chenxuliang/Desktop/chen/图片/imooc2.png')

# value = 'register_email'
# driver_1 = driver.find_element(By.ID,value)
# print(driver_1)
# print('=-=-=')
# user_name_element_note = driver.find_elements(By.CLASS_NAME,'controls')[1]
# # user_name_element_note_to_click = user_name_element_note[1]
# # user_name_element_note = driver.find_element(By.ID,'register_nickname')
#
# user_element = user_name_element_note.find_element(By.CLASS_NAME,'form-control')
# user_element.send_keys('ererere')
# driver.find_element(By.NAME,'password').send_keys('123456')
# driver.find_element(By.XPATH,'//*[@id="captcha_code"]').send_keys('111111')
