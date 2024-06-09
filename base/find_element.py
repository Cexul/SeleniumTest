# coding:utf-8
from selenium import webdriver
from util.read_ini import ReadIni
from selenium.webdriver.common.by import By


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                # element_id = self.driver.find_element(By.ID, value)
                return self.driver.find_element(By.ID, value)

                # return self.driver.find_element(By.ID,value)
            elif by == 'name':
                return self.driver.find_element(By.NAME, value)
            elif by == 'className':
                return self.driver.find_element(By.CLASS_NAME, value)
            else:
                return self.driver.find_element(By.XPATH, value)
        except:
            # self.driver.save_screenshot()
            return None
        # if by == 'id':
        #     print('=-=-=-=')
        #     element_id = self.driver.find_element(By.ID, value)
        #     return element_id
        #
        #     # return self.driver.find_element(By.ID,value)
        # elif by == 'name':
        #     return self.driver.find_element(By.NAME, value)
        # elif by == 'className':
        #     return self.driver.find_element(By.CLASS_NAME, value)
        # else:
        #     return self.driver.find_element(By.XPATH, value)


# if __name__ == '__main__':
#     options = webdriver.EdgeOptions()
#     options.add_experimental_option('detach', True)
#     driver = webdriver.Edge(options=options)
#     driver.get('http://www.5itest.cn/register')
#
#     find_element = FindElement(driver)
#     user_element = find_element.get_element('user_email')
#     print(user_element)
