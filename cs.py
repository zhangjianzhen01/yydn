import requests

rkd = ['RK22110151']
rkdid = []
xlhid=[]
xlh=[]
ddh=[]
from business import denglu

tk = denglu.test_dlxt()
# 订单号搜索
for z in rkd:
    cx_url = f'http://192.168.0.217:9090/EnterOrder?order_sn={z}&link_order_sn=&business_no=&voucher_abstract=&customer_name=&status=&type=&source=&sortField=&sortOrder='
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    x = r.json()['data'][0]['id']
    rkdid.append(r.json()['data'][0]['id'])
    # print(rkdid)

# 获取序列号列表
for c in rkdid:
    cx_url = f'http://192.168.0.217:9090/EnterOrder/{c}'
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    x = r.json()['data']['order_list'][0]['id']
    xlhid.append(r.json()['data']['order_list'][0]['id'])
    # print(xlhid)

# 请求序列号
for v in xlhid:
    cx_url = f'http://192.168.0.217:9090/EnterOrderItemVerify?order_item_id={v}&limit=100'
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    x = r.json()['data'][0]['serial_number']
    xlh.append(r.json()['data'][0]['serial_number'])
    print(xlh)

for num in xlh[0]:
    cx_url = f"http://192.168.0.217:9090/lc/purchaseDetail?purchase_order_code=&serial_number={num}&materiel_sn=&materiel_group_describe=&pn=&material_describe=&product_type=&sortField=&sortOrder="
    cx_head = {'Content-Type': 'application/json;charset=UTF-8', 'authorization': f'Bearer {tk}'}
    r = requests.get(url=cx_url, headers=cx_head, )
    x = r.json()
    ddh.append(r.json()['data'][0]['purchase_order_code'])
    print(ddh)