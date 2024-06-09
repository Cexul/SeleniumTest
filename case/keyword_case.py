# coding:utf-8

import sys
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod


class KeywordCase(object):

    def run_main(self):
        self.action_method = ActionMethod()

        handle_excel = ExcelUtil('/Users/chenxuliang/PycharmProjects/selenium/config/keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handel_value = handle_excel.get_col_value(i, 6)
                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)

                    # if send_value:
                    self.run_method(method, send_value, handel_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        # print(except_value)
                        if except_value[0] == 'text':
                            # print('-=-=-=-=-',except_result_method)
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                                # print('diyicixieru')
                                # print(i)
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            # print('============')
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                                # print('diercixieru')
                                # print(i)

                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')

    # 获取预期结果值
    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        # print(method_value)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
            # print('1')
        elif handle_value == '' and send_value == '':
            result = method_value()
            # print('2')
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
            # print('3')
        else:
            result = method_value(send_value,handle_value)
            # print('4')
        return result


if __name__ == '__main__':
    result = KeywordCase()
    result.run_main()
