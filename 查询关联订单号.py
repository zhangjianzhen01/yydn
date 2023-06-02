import requests
a = ['72MN135600911']
b = []
from business import denglu
tk = denglu.test_dlxt()

for num in a:
    cx_url = f"http://192.168.0.217:9090/lc/purchaseDetail?purchase_order_code=&serial_number={num}&materiel_sn=&materiel_group_describe=&pn=&material_describe=&product_type=&sortField=&sortOrder="
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    x = r.json()
    b.append(r.json()['data'][0]['purchase_order_code'])

print(b)