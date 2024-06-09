# -*- coding: utf-8 -*-

import json
import base64
import os
import ssl


try:
    from urllib.error import HTTPError
    from urllib.request import Request, urlopen
except ImportError:
    from urllib3 import Request, urlopen, HTTPError

context = ssl._create_unverified_context()


class Read_image(object):
    REQUEST_URL = "https://gjbsb.market.alicloudapi.com/ocrservice/advanced"
    params = {
        # 是否需要识别结果中每一行的置信度，默认不需要。 true：需要 false：不需要
        "prob": False,
        # 是否需要单字识别功能，默认不需要。 true：需要 false：不需要
        "charInfo": False,
        # 是否需要自动旋转功能，默认不需要。 true：需要 false：不需要
        "rotate": False,
        # 是否需要表格识别功能，默认不需要。 true：需要 false：不需要
        "table": False,
        # 字块返回顺序，false表示从左往右，从上到下的顺序，true表示从上到下，从左往右的顺序，默认false
        "sortPage": False,
        # 是否需要去除印章功能，默认不需要。true：需要 false：不需要
        "noStamp": False,
        # 是否需要图案检测功能，默认不需要。true：需要 false：不需要
        "figure": False,
        # 是否需要成行返回功能，默认不需要。true：需要 false：不需要
        "row": False,
        # 是否需要分段功能，默认不需要。true：需要 false：不需要
        "paragraph": False,
        # 图片旋转后，是否需要返回原始坐标，默认不需要。true：需要  false：不需要
        "oricoord": True
    }

    def get_img(self,img_file):
        """将本地图片转成base64编码的字符串，或者直接返回图片链接"""
        # 简单判断是否为图片链接
        if img_file.startswith("http"):
            return img_file
        else:
            with open(os.path.expanduser(img_file), 'rb') as f:  # 以二进制读取本地图片
                data = f.read()
        try:
            encodestr = str(base64.b64encode(data), 'utf-8')
        except TypeError:
            encodestr = base64.b64encode(data)

        return encodestr


    def posturl(self,headers, body):
        """发送请求，获取识别结果"""
        try:
            params = json.dumps(body).encode(encoding='UTF8')
            req = Request(self.REQUEST_URL, params, headers)
            r = urlopen(req, context=context)
            html = r.read()
            return html.decode("utf8")
        except HTTPError as e:
            print(e.code)
            print(e.read().decode("utf8"))


    def request(self,img_file,appcode="47e86a62b9584086bb6206b1cfa74bf9"):
        # 请求参数
        if self.params is None:
            self.params = {}
        img = self.get_img(img_file)
        if img.startswith('http'):  # img 表示图片链接
            self.params.update({'url': img})
        else:  # img 表示图片base64
            self.params.update({'img': img})

        # 请求头
        headers = {
            'Authorization': 'APPCODE %s' % appcode,
            'Content-Type': 'application/json; charset=UTF-8'
        }

        response = self.posturl(headers, self.params)
        result = json.loads(response)

        return result['content']




# if __name__ == "__main__":
#     # 配置信息
#     # appcode = "47e86a62b9584086bb6206b1cfa74bf9"
#     # img_file = "/Users/chenxuliang/Desktop/chen/图片/imooc1.png"
#     # params = {
#     #     # 是否需要识别结果中每一行的置信度，默认不需要。 true：需要 false：不需要
#     #     "prob": False,
#     #     # 是否需要单字识别功能，默认不需要。 true：需要 false：不需要
#     #     "charInfo": False,
#     #     # 是否需要自动旋转功能，默认不需要。 true：需要 false：不需要
#     #     "rotate": False,
#     #     # 是否需要表格识别功能，默认不需要。 true：需要 false：不需要
#     #     "table": False,
#     #     # 字块返回顺序，false表示从左往右，从上到下的顺序，true表示从上到下，从左往右的顺序，默认false
#     #     "sortPage": False,
#     #     # 是否需要去除印章功能，默认不需要。true：需要 false：不需要
#     #     "noStamp": False,
#     #     # 是否需要图案检测功能，默认不需要。true：需要 false：不需要
#     #     "figure": False,
#     #     # 是否需要成行返回功能，默认不需要。true：需要 false：不需要
#     #     "row": False,
#     #     # 是否需要分段功能，默认不需要。true：需要 false：不需要
#     #     "paragraph": False,
#     #     # 图片旋转后，是否需要返回原始坐标，默认不需要。true：需要  false：不需要
#     #     "oricoord": True
#     # }
#
#     result = Read_image()
#     result.request(img_file="/Users/chenxuliang/Desktop/chen/图片/imooc1.png")