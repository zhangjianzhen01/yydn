import requests
from business import logger


# 登录系统
def test_dlxt():
    url = 'http://192.168.0.21:9090/login'
    head = {'Content-Type': 'application/json;charset=UTF-8'}
    data = {"username": "admin", "password": "huazhou666"}
    r = requests.post(url=url, headers=head, json=data)
    req=r.json()
    print(req)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    return r.json()['data']['token']


# test_dlxt()
