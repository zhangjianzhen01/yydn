import requests, random, datetime
from business import denglu
null=None

tk = denglu.test_dlxt()
qn_list=[]

def test_a():
    url = 'http://192.168.0.21:9090/SerialStock?page=1&limit=50&materiel_pcode=V00107D000000000&status=0'
    heads = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=url, headers=heads)
    data = r.json()['data']
    for item in data:
        qn = item['qn']
        qn_list.append(qn)
        qn_string = '\n'.join(qn_list)
    print(qn_string)
