# coding:utf-8

from base.find_element import FindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

    # 获取邮箱元素
    def get_email_element(self):
        email_element = self.fd.get_element('user_email')
        return email_element

    # 获取用户名元素
    def get_username_element(self):
        username_element = self.fd.get_element('user_name')
        return username_element

    # 获取用户名元素
    def get_password_element(self):
        password_element = self.fd.get_element('password')
        return password_element

    # 获取用户名元素
    def get_code_element(self):
        code_element = self.fd.get_element('code_text')
        return code_element

    # 获取按钮元素
    def get_button_element(self):
        button_element = self.fd.get_element('register_button')
        return button_element

    # 获取邮箱错误信息元素
    def get_email_error_element(self):
        email_error_element = self.fd.get_element('user_email_error')
        # print(email_error_element.get_attribute('value'))
        return email_error_element

    # 获取用户名错误信息元素
    def get_username_error_element(self):
        username_error_element = self.fd.get_element('user_name_error')
        return username_error_element

    # 获取密码错误信息元素
    def get_password_error_element(self):
        password_error_element = self.fd.get_element('password_error')
        return password_error_element

    # 获取验证码错误信息元素
    def get_code_error_element(self):
        code_error_element = self.fd.get_element('code_text_error')
        return code_error_element