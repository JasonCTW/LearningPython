'''
Author ：SunJie
接口请求，返回
'''
import requests
import json


class Request:
    def __init__(self, url, method, header, _json):
        self.url = url
        self.method = method
        self.header = header
        self.json = json.dumps(_json)

    def post(self):
        res = requests.post(url=self.url, data=self.json, headers=self.header)
        return res

    def get_data(self):
        if self.method == 'post':
            res = self.post()
            return res.text
        else:
            pass


if __name__ == '__main__':
    url = 'http://192.168.15.67:8090/rm-mras/merchant/v1/addprerisk'
    method = 'post'
    header = {'Content-Type':'application/json'}
    json_ = '../data/test.json'
    with open(json_, 'r') as load_f:
        load_dict = json.load(load_f)
    test = Request(url=url, method=method, header=header, _json=load_dict)
    print(test.get_data())