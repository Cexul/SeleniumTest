# coding = utf-8

from selenium import webdriver
import time
# driver = webdriver.Chrome('/Users/username/Downloads/chromedriver')
url = 'http://www.baidu.com' #通过get方法获取当前URL打印
browser = webdriver.Chrome()
browser.maximize_window()#设置浏览器最大化
second_url = 'http://www.bilibili.com'
browser.get(url)
time.sleep(1)
print("welcome %s" %(url))
print(browser.title)#打印网站title
browser.find_element_by_id("kw").send_keys("selenium")
time.sleep(1)
browser.find_element_by_id("su").click()
time.sleep(2)

browser.get(second_url)
time.sleep(1)

browser.back()
time.sleep(1)

browser.forward()
time.sleep(1)
browser.close()